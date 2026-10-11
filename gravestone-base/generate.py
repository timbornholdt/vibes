# Generates the gravestone base STLs (viewer: index.html in this folder).
# Usage: pip install manifold3d trimesh && python3 generate.py
#   -> gravestone-base.stl  the full base (print 2 per stone)
#   -> fit-test.stl         a short slice of the same slot, set screw and captive-nut slot
# Tweak SLOT for fit; STONE is the measured gravestone thickness.
# X = front/back (tip direction), Y = along stone width, Z = up. mm.
import os, numpy as np, trimesh
from manifold3d import Manifold, CrossSection

STONE = 39.69          # 1 18/32"
SLOT = 42.5            # loose fit, set screw takes up the gap
L, W, T = 240.0, 90.0, 7.0   # plate
WALL = 14.0                  # socket wall thickness
GUS_T, GUS_X = 8.0, 95.0     # gusset thickness, reach
STAKE_X, STAKE_Y, STAKE_W, STAKE_L = 108.0, 22.0, 9.0, 34.0
CH = 3.0                     # slot lead-in chamfer
NUT_AF, NUT_TH, NUT_AC = 10.0, 5.0, 11.55   # M6 hex nut
SEG = 64

def box(x0, x1, y0, y1, z0, z1):
  return Manifold.cube([x1 - x0, y1 - y0, z1 - z0]).translate([x0, y0, z0])

def stadium(w, l, h):
  # rounded slot, long along Y
  c = CrossSection.circle(w / 2, SEG)
  return CrossSection.batch_hull([c.translate([0, -(l - w) / 2]), c.translate([0, (l - w) / 2])]).extrude(h)

def base(H=70.0, screw_z=T + 35.0):
  # H: socket wall height above the plate; screw_z: height of the set screw axis
  r = 12.0
  corners = [CrossSection.circle(r, SEG).translate([sx * (L / 2 - r), sy * (W / 2 - r)]) for sx in (-1, 1) for sy in (-1, 1)]
  body = CrossSection.batch_hull(corners).extrude(T)

  xi, xo = SLOT / 2, SLOT / 2 + WALL
  body += box(-xo, -xi, -W / 2, W / 2, 0, T + H) + box(xi, xo, -W / 2, W / 2, 0, T + H)

  for s in (-1, 1):
    for y in (-W / 2, W / 2 - GUS_T):
      g = CrossSection([[[0, 0], [GUS_X - xo, 0], [0, H - 4]]]).extrude(GUS_T)  # triangle in (x,z)
      g = g.rotate([90, 0, 0]).translate([0, GUS_T, 0])                          # stand it up in XZ
      if s < 0:
        g = g.mirror([1, 0, 0])
      body += g.translate([s * xo, y, T])

  # slot (clears down to plate top) + lead-in chamfers along the top inner edges
  body -= box(-xi, xi, -W, W, T, T + H + 1)
  for s in (-1, 1):
    ch = Manifold.cube([CH * 1.4142, 2 * W, CH * 1.4142], center=True).rotate([0, 45, 0])
    body -= ch.translate([s * xi, 0, T + H])

  for sx in (-1, 1):
    for sy in (-1, 1):
      body -= stadium(STAKE_W, STAKE_L, T + 2).translate([sx * STAKE_X, sy * STAKE_Y, -1])

  # M6 set screw through +X wall; the nut drops into a slot from the top so it's captive
  body -= Manifold.cylinder(WALL + 10, 6.6 / 2, 6.6 / 2, SEG).rotate([0, 90, 0]).translate([xi - 5, 0, screw_z])
  nx = (xi + xo) / 2
  body -= box(nx - (NUT_TH + 0.5) / 2, nx + (NUT_TH + 0.5) / 2, -(NUT_AC + 0.5) / 2, (NUT_AC + 0.5) / 2,
              screw_z - (NUT_AF + 0.4) / 2, T + H + 1)
  return body

def fit_test():
  # A 30 mm slice of the socket: both slot walls (same slot width, chamfer and wall
  # thickness as the real part), the bolt hole and the drop-in nut slot. Checks the
  # stone fit and the nut/bolt fit for ~10% of the filament of a full base.
  b = base(H=24.0, screw_z=T + 12.0)
  xo = SLOT / 2 + WALL
  return b ^ box(-xo - 1, xo + 1, -8, 22, -1, 100)

def save(m, path):
  m = m.to_mesh()
  mesh = trimesh.Trimesh(vertices=np.asarray(m.vert_properties)[:, :3], faces=np.asarray(m.tri_verts))
  print(os.path.basename(path), "watertight", mesh.is_watertight, "volume cm3", round(mesh.volume / 1000, 1),
        "bounds", mesh.bounds.round(2).tolist())
  mesh.export(path)

if __name__ == "__main__":
  here = os.path.dirname(os.path.abspath(__file__))
  save(base(), os.path.join(here, "gravestone-base.stl"))
  save(fit_test(), os.path.join(here, "fit-test.stl"))
