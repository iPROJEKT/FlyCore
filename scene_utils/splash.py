from panda3d.core import (
    loadPrcFileData,
    WindowProperties,
    TransparencyAttrib,
)
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenImage import OnscreenImage
from direct.task import Task

class SplashScreen:
    def __init__(self, base: ShowBase, image_path: str, duration: float = 3.0, on_finish=None):
        self.base = base
        self.on_finish = on_finish

        # Создаём временное окно для сплеш-скрина
        props = WindowProperties()
        props.setSize(800, 300)  # Укажи нужный размер
        props.setUndecorated(True)  # Убирает рамку и заголовок
        props.setTitle("Fly Pro by AERO")
        self.base.openDefaultWindow(props=props)

        # Фон чёрный (или любой другой)
        self.base.setBackgroundColor(0, 0, 0, 1)

        # Изображение по центру
        self.image = OnscreenImage(
            image=image_path,
            pos=(0, 0, 0),
            scale=1,  # Подгони под размер окна или укажи явно, например (0.5, 1, 0.5)
            parent=self.base.render2d
        )
        self.image.setTransparency(TransparencyAttrib.MAlpha)

        # Рендерим пару кадров, чтобы изображение появилось
        self.base.graphicsEngine.renderFrame()
        self.base.graphicsEngine.renderFrame()

        # Запускаем таймер
        self.base.taskMgr.doMethodLater(duration, self.finish_splash, "finish_splash")

    def finish_splash(self, task: Task):
        self.image.destroy()
        self.image = None

        if self.on_finish:
            self.on_finish()

        return Task.done