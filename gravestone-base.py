# Generates gravestone-base.stl (viewer: gravestone-base.html).
# Usage: pip install manifold3d trimesh && python3 gravestone-base.py gravestone-base.stl
# Tweak SLOT for fit; STONE is the measured gravestone thickness.
# Gravestone base generator. X = front/back (tip direction), Y = along stone width, Z = up. mm.
import sys, numpy as np, trimesh
from manifold3d import Manifold, CrossSection

STONE = 39.69          # 1 18/32"
SLOT = 42.5            # loose fit, set screw takes up the gap
L, W, T = 240.0, 90.0, 7.0   # plate
WALL, H = 14.0, 70.0         # socket wall thickness, height above plate
GUS_T, GUS_X = 8.0, 95.0     # gusset thickness, reach
STAKE_X, STAKE_Y, STAKE_W, STAKE_L = 108.0, 22.0, 9.0, 34.0
SCREW_Z = T + 35.0
CH = 3.0                     # slot lead-in chamfer
SEG = 64

def box(x0, x1, y0, y1, z0, z1):
  return Manifold.cube([x1 - x0, y1 - y0, z1 - z0]).translate([x0, y0, z0])

def stadium(w, l, h):
  # rounded slot, long along Y
  c = CrossSection.circle(w / 2, SEG)
  return CrossSection.batch_hull([c.translate([0, -(l - w) / 2]), c.translate([0, (l - w) / 2])]).extrude(h)

r = 12.0
corners = [CrossSection.circle(r, SEG).translate([sx * (L / 2 - r), sy * (W / 2 - r)]) for sx in (-1, 1) for sy in (-1, 1)]
plate = CrossSection.batch_hull(corners).extrude(T)

xi, xo = SLOT / 2, SLOT / 2 + WALL
walls = box(-xo, -xi, -W / 2, W / 2, 0, T + H) + box(xi, xo, -W / 2, W / 2, 0, T + H)

gussets = []
for s in (-1, 1):
  for y in (-W / 2, W / 2 - GUS_T):
    tri = CrossSection([[[0, 0], [GUS_X - xo, 0], [0, H - 4]]])  # in (x,z)
    g = tri.extrude(GUS_T)                      # extruded along Z -> rotate so it stands in XZ
    g = g.rotate([90, 0, 0]).translate([0, GUS_T, 0])  # now x->x, extrude->y, z->z
    if s < 0:
      g = g.mirror([1, 0, 0])
    gussets.append(g.translate([s * xo, y, T]))
body = plate + walls
for g in gussets:
  body += g

# slot (clears down to plate top) + lead-in chamfers along the top inner edges
body -= box(-xi, xi, -W, W, T, T + H + 1)
for s in (-1, 1):
  ch = Manifold.cube([CH * 1.4142, 2 * W, CH * 1.4142], center=True).rotate([0, 45, 0])
  body -= ch.translate([s * xi, 0, T + H])

# stake slots
for sx in (-1, 1):
  for sy in (-1, 1):
    body -= stadium(STAKE_W, STAKE_L, T + 2).translate([sx * STAKE_X, sy * STAKE_Y, -1])

# M6 set screw through +X wall, nut drops into a slot from the top
hole = Manifold.cylinder(WALL + 10, 6.6 / 2, 6.6 / 2, SEG).rotate([0, 90, 0]).translate([xi - 5, 0, SCREW_Z])
body -= hole
NUT_AF, NUT_TH, NUT_AC = 10.0, 5.0, 11.55
nx = (xi + xo) / 2
body -= box(nx - (NUT_TH + 0.5) / 2, nx + (NUT_TH + 0.5) / 2, -(NUT_AC + 0.5) / 2, (NUT_AC + 0.5) / 2, SCREW_Z - (NUT_AF + 0.4) / 2, T + H + 1)

m = body.to_mesh()
mesh = trimesh.Trimesh(vertices=np.asarray(m.vert_properties)[:, :3], faces=np.asarray(m.tri_verts))
print("watertight", mesh.is_watertight, "volume cm3", round(mesh.volume / 1000, 1), "bounds", mesh.bounds.round(2).tolist(), "tris", len(mesh.faces))
mesh.export(sys.argv[1])
