from graphics import *
from random import randint

def main():

    WIDTH = 800
    HEIGHT = 600

    win = GraphWin("Lewis and Clark", WIDTH, HEIGHT)
    #bg = Image(Point(WIDTH/2, HEIGHT/2), "art.pbm")
    win.setBackground(color_rgb(15, 15, 15))

    # Setting up the title screen
    title = Text(Point(WIDTH/2, 100), "The Lewis and Clark Expedition")
    title.setTextColor(color_rgb(255, 255, 255))
    title.setSize(20)
    title.setFace('courier')
    title.draw(win)

    kcheck = win.checkKey()
    win.getKey()
    if kcheck == "Return":
        intro = Text(Point(WIDTH/2, 200), """Shortly after the Louisiana purchase
        Thomas Jefferson institued an expedition to explore
        the newly acquired territory.""")
        intro.setTextColor(color_rgb(255, 255, 255))
        intro.setFace('courier')
        intro.draw(win)
    else:
        intro = Text(Point(WIDTH/2, 200), """Shortly after the Louisiana purchase
        Thomas Jefferson institued an expedition to explore
        the newly acquired territory.""")
        intro.setTextColor(color_rgb(255, 255, 255))
        intro.setFace('courier')
        intro.draw(win)

        win.getKey()

    if kcheck == "Return":
        intro1 = Text(Point(WIDTH/2, 400), """Your job is to make it through Illinois, Missouri,
        Kansas, Iowa, Nebraska, South Dakota, North Dakota, Montana, Idaho, Oregon, and Washington.""")
        intro1.setTextColor(color_rgb(255, 255, 255))
        intro1.setFace('courier')
        intro1.draw(win)
    else:
        intro1 = Text(Point(WIDTH/2, 300), """Your job is to make it through Illinois, Missouri,
        Kansas, Iowa, Nebraska, South Dakota, North Dakota, Montana,
        Idaho, Oregon, and Washington.""")
        intro1.setTextColor(color_rgb(255, 255, 255))
        intro1.setFace('courier')
        intro1.draw(win)

        win.getKey()

        intro2 = Text(Point(WIDTH/2, 450), "Enter your name")
        intro2.setTextColor(color_rgb(255, 255, 255))
        intro2.setFace('courier')
        intro2.draw(win)
        user_input = Entry(Point(WIDTH/2, 500), 20)
        user_input.draw(win)

    # Collecting username and storing data
    while True:
        if win.checkKey() == "Return":
            name = user_input.getText()
            score = 0
            players = dict()
            players[name] = score
            title.undraw()
            intro.undraw()
            intro1.undraw()
            user_input.undraw()
            intro2.undraw()

            break

    # Important Objects
    class Gun:

        def __init__(self, price, has):
            self.price = price
            self.has = has

    rifle = Gun(350, False)

    class Eat:

        def __init__(self, price, amount):
            self.price = price
            self.amount = amount

    food = Eat(150, 0)

    class Animal:

        def __init__(self, price, has):
            self.price = price
            self.has = has

    mule = Animal(300, False)

    money = 550

            # Camp Dubois Shop
    dubois = Text(Point(WIDTH/2, 100), """To begin your journey please buy some starting gear.""")
    dubois.setTextColor(color_rgb(255, 255, 255))
    dubois.setFace('courier')
    dubois.setSize(15)
    dubois.draw(win)
    dubois_header = Text(Point(WIDTH/2, 40), """Camp Dubois Shop""")
    dubois_header.setTextColor(color_rgb(255, 0, 0))
    dubois_header.setFace('courier')
    dubois_header.setSize(18)
    dubois_header.draw(win)

    dubois_shop = Text(Point(200, 250), """
                                1. 10 pounds of mixed foods. (A pound per a day.) $150


                                2. Two Horses.                                        $300


                                3. Model 1803 muzzle-loading .54 caliber rifle.   $350


                      """)
    dubois_shop.setTextColor(color_rgb(255, 50, 50))
    dubois_shop.setFace('courier')
    dubois_shop.setSize(15)
    dubois_shop.draw(win)

    dubois_money = Text(Point(WIDTH/2, 400), """Money: $"""+ str(money))
    dubois_money.setTextColor(color_rgb(250, 210, 0))
    dubois_money.setFace('courier')
    dubois_money.setSize(15)
    dubois_money.draw(win)

            # User input Box

    option = Entry(Point(WIDTH/2, 350), 20)
    option.draw(win)


    while True:
        if money <= 0:
            money = 0
            option.setText("")
            dubois_money.undraw()
            dubois_money = Text(Point(WIDTH/2, 400), """Money: $"""+ str(money))
            dubois_money.setTextColor(color_rgb(250, 210, 0))
            dubois_money.setFace('courier')
            dubois_money.setSize(15)
            dubois_money.draw(win)

            break

        buy = option.getText()
        if win.checkKey() == 'Return':
            if buy == "1":
                if money >= food.price:
                    food.amount += 10
                    money -= food.price
                    option.setText("")
                    dubois_money.undraw()
                    dubois_money = Text(Point(WIDTH/2, 400), """Money: $"""+ str(money))
                    dubois_money.setTextColor(color_rgb(250, 210, 0))
                    dubois_money.setFace('courier')
                    dubois_money.setSize(15)
                    dubois_money.draw(win)
            elif buy == "2":
                if money >= mule.price:
                    mule.has = True
                    money -= mule.price
                    option.setText("")
                    dubois_money.undraw()
                    dubois_money = Text(Point(WIDTH/2, 400), """Money: $"""+ str(money))
                    dubois_money.setTextColor(color_rgb(250, 210, 0))
                    dubois_money.setFace('courier')
                    dubois_money.setSize(15)
                    dubois_money.draw(win)
            elif buy == "3":
                if money >= rifle.price:
                    rifle.has = True
                    money -= rifle.price
                    option.setText("")
                    dubois_money.undraw()
                    dubois_money = Text(Point(WIDTH/2, 400), """Money: $"""+ str(money))
                    dubois_money.setTextColor(color_rgb(250, 210, 0))
                    dubois_money.setFace('courier')
                    dubois_money.setSize(15)
                    dubois_money.draw(win)
        elif money == 50 or money == 100:
            next = Text(Point(WIDTH/2, HEIGHT/2), "Press any key to continue.")
            next.setFace('courier')
            next.setTextColor(color_rgb(255, 255, 255))
            next.setSize(15)
            next.draw(win)
            dubois_money.undraw()
            option.undraw()
            dubois_header.undraw()
            dubois_shop.undraw()
            dubois.undraw()

            break

    win.getKey()

    Injury = Image(Point(WIDTH/2, HEIGHT/2), "Injury.pbm")
    next.undraw()
    Injury.draw(win)

    appendix = Text(Point(WIDTH/2, HEIGHT/2), """August 20 1804: One of your Sergeants has appendicitis.
    Would you like to leave him? (Yes/No)""")
    appendix.setFace('courier')
    appendix.setTextColor(color_rgb(255, 255, 255))
    appendix.setSize(15)
    appendix.draw(win)

    yes_no = Entry(Point(WIDTH/2, 350), 20)
    yes_no.draw(win)

    while True:

        yn = yes_no.getText()
        if win.checkKey() == 'Return':
            if yn.lower() == "no":
                Injury.undraw()
                appendix.undraw()
                yes_no.undraw()
                sergeant = Text(Point(WIDTH/2, HEIGHT/2), """He dies anyway. You burry him in what is now Floyd's River,
        named after him in respect.""")
                sergeant.setFace('courier')
                sergeant.setTextColor(color_rgb(255, 255, 255))
                sergeant.draw(win)
                break
            elif yn.lower() == "yes":
                Injury.undraw()
                appendix.undraw()
                yes_no.undraw()
                sergeant = Text(Point(WIDTH/2, HEIGHT/2), """You burry him in what is now Floyd's River,
        named after him in respect.""")
                sergeant.setFace('courier')
                sergeant.setTextColor(color_rgb(255, 255, 255))
                sergeant.draw(win)
                break
            elif yn.lower() != "yes" or "no":
                yes_no.setText(yn)


    win.getKey()

    sergeant.undraw()
    indian = Text(Point(WIDTH/2, 100), """November 4 1804: You come across  Toussaint Charbonneau,
    who is a French Canadian fur trader.""")
    indian.setFace('courier')
    indian.setTextColor(color_rgb(255, 255, 255))
    indian.draw(win)

    win.getKey()

    indian1 = Text(Point(WIDTH/2, 200), """He and his wife known as Sacagawea, a Shoshone indian, join you
    you on your journy.""")
    indian1.setFace('courier')
    indian1.setTextColor(color_rgb(255, 255, 255))
    indian1.draw(win)

    win.getKey()

    indian2 = Text(Point(WIDTH/2, 300), """This is a good decision due to the fact that you may encounter other
    Shoshone indians, who could be of use.""")
    indian2.setFace('courier')
    indian2.setTextColor(color_rgb(255, 255, 255))
    indian2.draw(win)

    win.getKey()

    indian.undraw()
    indian1.undraw()
    indian2.undraw()
    rattle = Text(Point(WIDTH/2, 300), """Febuary 11 1805: Sacagawea is about to give birth,
     you need to crush a rattle snake
     to make some medicine for her.""")
    rattle.setSize(15)
    rattle.setFace('courier')
    rattle.setTextColor(color_rgb(255, 255, 255))
    rattle.draw(win)

    win.getKey()

    rattle.undraw()

    if rifle.has == False:
        killint = Text(Point(WIDTH/2, 200), """The snake attacks Lewis, he dies.
        The expedition is cancelled.""")
        killint.setFace('courier')
        killint.setTextColor(color_rgb(255, 255, 255))
        killint.draw(win)
        win.getKey()
        win.close()
    elif rifle.has == True:
        kill = Text(Point(WIDTH/2, 200), """You shoot a snake with your rifle,
    you successfully produce medicine. Sacagawea
    gives birth to Jean Baptiste.""")
        kill.setFace('courier')
        kill.setTextColor(color_rgb(255, 255, 255))
        kill.draw(win)

    win.getKey()
    kill.undraw()

    r = randint(0, 20)

    river = Text(Point(WIDTH/2, 200), """ 1805: You approach Judith river,
    and begin to strap down your supplies to the horses.""")
    river.setFace('courier')
    river.setTextColor(color_rgb(255, 255, 255))
    river.draw(win)

    win.getKey()

    if r < 10:
        cross = Text(Point(WIDTH/2, 200), """The river is to deep,
        you lose all of your supplies and are forced to end the expedition.""")
        cross.setFace('courier')
        cross.setTextColor(color_rgb(255, 255, 255))
        cross.draw(win)
        river.undraw()
        win.getKey()
        win.close()
    elif r >= 10:
        cross = Text(Point(WIDTH/2, 200), """You successfully cross the Judith,
        you lose no supplies.""")
        cross.setFace('courier')
        cross.setTextColor(color_rgb(255, 255, 255))
        cross.draw(win)
        river.undraw()

    win.getKey()
    win.close()
main()
