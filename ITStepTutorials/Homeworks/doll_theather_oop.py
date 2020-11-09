"""
ТЗ: необходимо построить архитектуру приложения "Кукольный театр". 
Субъекты кукольного театра: 
    1. Кукловод
        имеет свойства: имя, тип голоса, талант (1-10), куклы.
        умеет: запускать выступление куклы.
    2. Кукла
        имеет свойства: имя, тип, пол, возраст, цвет.
        умеет: выступать
    3. Постановка
        имеет свойства: кукловоды
        умеет: запускать выступление Кукловода
    4. Зритель.
        умеет: аплодировать.
    5. Сцена
        свойства: Постановка, Зрители.
        умеет: запускать Постановку.

2. Собрать кукольный театр и запустить представление.
"""
class Puppeteer:
    
    def __init__(self, name: str, voice: str, talant: str, dolls: list):
        self._name = name
        self._voice = voice
        self._talant = talant
        self._dolls = dolls

    def play_with_dolls(self):
        print(f'🧙‍♂️ - {self._name} talanted in {self._talant} with {self._voice} voice is playing with:')
        for doll in self._dolls:
            doll.act_on()


class Puppet:

    def __init__(self, name: str, type_of: str, gender: str, age: int, color: str):
        self._name = name
        self._type = type_of
        self._gender = gender
        self._age = age
        self._color = color

    def act_on(self):
        print(f'\t🤡 {self._name} {self._gender} {self._type} is {self._age}yo and {self._color}')


class Stage:
    
    def __init__(self, puppeteers: list):
        self._puppeteers = puppeteers

    def run_puppeteers(self):
        for puppeteer in self._puppeteers:
            puppeteer.play_with_dolls()


class Viewer:

    count = 0

    def __init__(self):
        Viewer.count += 1
        self._id = Viewer.count
    
    def applaud(self):
        print(f'👏Viewer {self._id} is applauding loudly👏')


class Scene:
    
    def __init__(self, stage: Stage, viewers: list):
        self._stage = stage
        self._viewers = viewers

    def run_stage(self):
        print('\nScene has been started!\n')
        self._stage.run_puppeteers()
        print('\nApplause:')
        for v in self._viewers:
            v.applaud()


# Initialization of puppets and puppeteers
puppeteers = []
puppets1 = [ Puppet('Micky', 'wooden', 'male', 10, 'brown'),
             Puppet('Cam', 'paper', 'female', 12, 'red'), Puppet('Mon', 'wooden', 'male', 11, 'orange') ]
puppeteers.append(Puppeteer('Max', 'bass', '3 puppets in one time', puppets1))
puppets2 = [ Puppet('Moron', 'metal', 'female', 14, 'grey'),
             Puppet('Conny', 'paper', 'male', 19, 'white') ]
puppeteers.append(Puppeteer('Veronica', 'high', 'wide range of voice', puppets2))

# Initialization of the stage and viewers
stage = Stage(puppeteers=puppeteers)
viewers = [ Viewer() for v in range(5) ]

# Running the scene
scene = Scene(stage, viewers)
scene.run_stage()
