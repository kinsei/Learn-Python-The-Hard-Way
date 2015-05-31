# this is exercise 43 from the book Learn Python The Hard Way by Zed Shaw

class Scene(object):
    
    def enter(self):
        print "this scene is not yet configured. subclass it and implement enter()"

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        while True:
            print "\n--------------"
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)


class Death(Scene):
  
    quips = [
            "You died. You kind of suck at this.",
            "Your mom would be proud...if she were smatrer",
            "Such a luser.",
            "I have a small puppy thats better atthis>"
             ]
    def enter(self):
        print Death.quips[randint(0, len(self.quips) = 1)]
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        print"The Gothons of planet Percal #25 have invaded your ship and destroyed"
        print"your entire crew. You are the last surviving member and your last"
        print"mission is to get the neutron destruct bomb from the weapons armory,"
        print"put ryit in the bridge, and blow the ship up after getting into an"
        print"escape pod."
        print"\n"
        print"Your running down the central corridor to the weapons armory when"
        print"a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume"
        print"flowing around his hate filled body. He's blocking the door to the"
        print"Armory and about to pull a weapon to blast you"
        
        action = raw_input(">>>")

        if action == "shoot!":
            print "quick on the draw you yank out your blaster and fire it at the Gothon"
            print "his clown costume is flowing and moving around his body, which throughs"
            print" off youe aim. Your laser hits his costume but mimsses him entirly. this"
            print"completely ruins his brand new costume his mother boughthim, wich"
            print" makes him fly into a rage and blast you repeatedly in the face untill"
            print" your dead. then he eats you."
            return 'death'

        elif action == "dodge!":
            print "Like a world class boxer you dodge, weave, ,slip and slide right"
            print "as the Gothon's blaster cranks a laser past your head."
            print "In the middle of the artful dodge your foot slips and you"
            print "bang your head on the metal wall and pass out"
            print "You wake up shortly after only to die as the Gothon stomps on"
            print "your head and eats you"
            return 'death'
            

        elif action =="tell a joke":
            print "Lucky for you they made you learn Gothon insults in the academy"
            print " You tell the one Gothon joke you know:"
            print "Lndef jcn kfvwdv efacv fsvdg qfd, dgjdsa wcscx cvfewf."
            print "The gothon stops, tries not to laugh, then burst out laughing and cant mov"
            print "While he's laughing you run up and shoot him square in the head"
            print "putting him down, then jumping through the weapons armory door"
            return 'laser_weapon_armory'

        else:
            print "Does not compute"
            return 'central_corridor'



class LaserWeaponArmory(Scene):
    
    def enter(self):
        print "You do a dive roll into the weapon armory, crouch and scan the room"
        print "for more Gothons that might be hiding. Its dead quiet, too quiet."
        print "You stand up and run to the far side of the room and find the"
        print "netron bomb in its container. Theres a keypad lock on the nox"
        print "and you need the code to get the nomb out. If you get the code"
        print "wrong 10 times then the lock closes forever and you can't"
        print "get the bomb. the code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0 

        while guesses != code and guesses < 10:
            print "BZZZZEDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")
            
        if guess == code:
            print "The container clicks open and the seal breaks, letting gas out."
            print " You grab the neutron bomb and run as fast as you you can to the"
            print "bridge where you must place it in the right spot."
            return 'the_bridge'
        else:
            print "The lock buzzes one last time and then you hear a sickining"
            print "melting sound as the mechanism is fused together."
            print "You decide to sit there, and finally the Gothons blow up the"
            print "ship from their ship and you die."
            return 'death'

class TheBridge(Scene):

    def enter(self):
        print "You burst onto the bridge with the neutron destruction bomb"
        print "under your arm and surprise 5 Gothons who are trying to"
        print "take control of the ship. Each of them has an even uglier"
        print "clown costume than the last. They haven't pilled theris"
        print "weapons out yet, as they see the active bomc under your"
        print "arm and don't wantto set it off."

class EscapePod(Scene):
   
    def enter(self):
        print "You rush through the ship desperatly trying to make it to"
        print "the escape pod befot the whole ship explodes. It seems like"
        print "hardly any Gothons are on the ship, so your run is clear of"
        print "interferance. ou get to the chamber with the escape pods, and"
        print "now need to pick one to take. Some of them could be damaged"
        print " but you don't have time to look. There's 5 pods, which one"
        print "do you take?"

        good_pod = randint(1,5)
        guess = raw_input("[pod #]> ")

        if int(guess) != good_pod:
            print "You jump intopod %s and hit the eject button." % guess
            print "The pod escapes out into the void of space, then"
            print "implodes as the hull ruptures, crushing your body"
            print "into jam jelly."
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "The pod easily slides out into space heading to"
            print "the planes below.As it flies to the planet, you look"
            print "back and see your ship implode then explode like a"
            print "bright star, taking out the Gothon ship at the same"
            print "time. You won!"
            return 'finished'

class Map(object):

    scenes = [
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    ]

    def __init___(self, start_scene):
        self.start_scene =start_scene
    
    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()

        
