"""
Just a guy with dots and lines
"""
from rubicon.java import JavaClass, JavaInterface
import toga
import toga_android.widgets.base

CustomView = JavaClass('org/beeware/android/CustomView')
IView = JavaInterface('org/beeware/android/IView')
Color = JavaClass("android/graphics/Color")
Paint = JavaClass("android/graphics/Paint")


class PlatformIndependentCanvasWidget:
    @property
    def _impl(self):
        impl = getattr(self, '__impl', None)
        if impl is None:
            self.__impl = CanvasWidget()
        return self.__impl


class CanvasWidget:
    def __init__(self):
        super().__init__()
        self.custom_view = CustomView(toga_android.widgets.base._get_activity().getApplicationContext())
        self.custom_view.setView(MicroCustomCanvasView())

    @property
    def native(self):
        return self.custom_view


class MicroCustomCanvasView(IView):
    def onDraw(self, canvas):
        paint = Paint()
        paint.setColor(Color.BLACK)
        paint.setAntiAlias(True)
        paint.setStrokeWidth(5.0)
        canvas.drawOval(0.0, 0.0, 400.0, 400.0, paint)


class MicroCustomCanvas(toga.App):
    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        main_canvas = PlatformIndependentCanvasWidget()
        self.main_window.content = main_canvas
        self.main_window.show()


def main():
    return MicroCustomCanvas()
