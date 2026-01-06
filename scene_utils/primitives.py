from panda3d.core import NodePath, TransparencyAttrib, AntialiasAttrib, LineSegs


def create_grid_floor(
    size: float = 300,
    step: float = 10,
    z_level: float = 0,
    color=(1, 1, 1, 1),
    alpha: float = 0.15,
    thickness: int = 2
) -> NodePath:
    lines = LineSegs("grid_floor")
    lines.setColor(*color)
    lines.setThickness(thickness)

    half_size = size / 2
    start = -half_size
    end = half_size
    num_lines = int(size // step) + 1

    for i in range(num_lines):
        pos = start + i * step
        lines.moveTo(start, pos, z_level)
        lines.drawTo(end, pos, z_level)

    for i in range(num_lines):
        pos = start + i * step
        lines.moveTo(pos, start, z_level)
        lines.drawTo(pos, end, z_level)

    node = NodePath(lines.create())
    node.setName("GridFloor")
    node.setTransparency(TransparencyAttrib.MAlpha)
    node.setAlphaScale(alpha)
    node.setAntialias(AntialiasAttrib.MLine)
    node.setLightOff(1)
    node.setBin("background", 0)
    node.setDepthWrite(False)

    return node


def create_box(
    size: float = 500,
    color=(0.8, 0.8, 1.0, 0.7),
    thickness: int = 2
) -> NodePath:
    h = size / 2.0
    lines = LineSegs("box_wireframe")
    lines.setColor(*color)
    lines.setThickness(thickness)

    edges = [
        ((-h, -h, -h), ( h, -h, -h)),
        (( h, -h, -h), ( h,  h, -h)),
        (( h,  h, -h), (-h,  h, -h)),
        ((-h,  h, -h), (-h, -h, -h)),

        ((-h, -h,  h), ( h, -h,  h)),
        (( h, -h,  h), ( h,  h,  h)),
        (( h,  h,  h), (-h,  h,  h)),
        ((-h,  h,  h), (-h, -h,  h)),

        ((-h, -h, -h), (-h, -h,  h)),
        (( h, -h, -h), ( h, -h,  h)),
        (( h,  h, -h), ( h,  h,  h)),
        ((-h,  h, -h), (-h,  h,  h)),
    ]

    for start, end in edges:
        lines.moveTo(*start)
        lines.drawTo(*end)

    node = NodePath(lines.create())
    node.setName("SimpleBox")
    node.setPos(0, 0, h)
    node.setTransparency(TransparencyAttrib.MAlpha)
    node.setAntialias(AntialiasAttrib.MLine)
    node.setLightOff(1)
    node.setBin("fixed", 10)

    return node


def create_rect_box(
    width: float,
    length: float,
    height: float,
    color=(0.8, 0.8, 1.0, 0.7),
    thickness: int = 2
) -> NodePath:
    hx = width / 2.0
    hy = length / 2.0
    hz = height / 2.0

    lines = LineSegs("rect_box_wireframe")
    lines.setColor(*color)
    lines.setThickness(thickness)

    edges = [
        # Bottom rectangle
        ((-hx, -hy, -hz), ( hx, -hy, -hz)),
        (( hx, -hy, -hz), ( hx,  hy, -hz)),
        (( hx,  hy, -hz), (-hx,  hy, -hz)),
        ((-hx,  hy, -hz), (-hx, -hy, -hz)),

        # Top rectangle
        ((-hx, -hy,  hz), ( hx, -hy,  hz)),
        (( hx, -hy,  hz), ( hx,  hy,  hz)),
        (( hx,  hy,  hz), (-hx,  hy,  hz)),
        ((-hx,  hy,  hz), (-hx, -hy,  hz)),

        # Vertical edges
        ((-hx, -hy, -hz), (-hx, -hy,  hz)),
        (( hx, -hy, -hz), ( hx, -hy,  hz)),
        (( hx,  hy, -hz), ( hx,  hy,  hz)),
        ((-hx,  hy, -hz), (-hx,  hy,  hz)),
    ]

    for start, end in edges:
        lines.moveTo(*start)
        lines.drawTo(*end)

    node = NodePath(lines.create())
    node.setName("RectBox")
    node.setPos(0, 0, hz)
    node.setTransparency(TransparencyAttrib.MAlpha)
    node.setAntialias(AntialiasAttrib.MLine)
    node.setLightOff(1)
    node.setBin("fixed", 10)

    return node