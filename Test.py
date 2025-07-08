from direct.showbase.ShowBase import ShowBase
from direct.showbase.ShowBaseGlobal import globalClock
from direct.task import Task
from panda3d.core import Vec3

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        environnent = self.loader.loadModel('models/environment')
        environnent.reparentTo(self.render)

        self.panda = self.loader.loadModel('models/panda-model')
        self.panda.reparentTo(self.render)
        self.panda.setPos(0, 5, 0)
        self.panda.setScale(0.05)

        self.disableMouse()
        self.camera.setPos(0, -40, 25)
        self.camera.lookAt(self.panda)

        self.keys = {"w": False,
                     "s": False,
                     "a": False,
                     "d": False}
        self.accept("w", self.set_key, ["w", True])
        self.accept("w-up", self.set_key, ["w", False])
        self.taskMgr.add(self.update_move, "update")

    def set_key(self, key, value):
        self.keys[key] = value

    def update_move(self, task):
        dt = globalClock.getDt()
        speed =50
        move_vec = Vec3(0,0,0)
        if self.keys["w"]:
            move_vec.y -= speed
        self.panda.setPos(self.panda.get_pos() + move_vec*dt)
        return Task.cont

        panda2 = self.loader.loadModel('models/panda-model')
        panda2.reparentTo(self.render)
        panda2.setPos(5, 5, 0)
        panda2.setScale(0.05)


game = Game()
game.run()