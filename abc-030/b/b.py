import sys
import math

n, m = sys.stdin.readline().rstrip().split(' ')
n = int(n)
m = int(m)

m_deg = 360.0 * m / 60
n_deg = 360.0 * n / 12 + 360.0 / 12 * m / 60

m_rad = m_deg * math.pi / 180.0
n_rad = n_deg * math.pi / 180.0

mx = math.cos(m_rad)
my = math.sin(m_rad)

nx = math.cos(n_rad)
ny = math.sin(n_rad)

mdn = mx * nx + my * ny
rad = math.acos(mdn)
deg = rad * 180.0 / math.pi

print deg
