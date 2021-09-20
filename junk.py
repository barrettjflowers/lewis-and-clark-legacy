lbox = Rectangle(Point(700, 500), Point(100, 525))
  lbox.setFill(color_rgb(255, 255, 255))
  lbox.draw(win)

  sbox = Rectangle(Point(350, 500), Point(450, 525))
  sbox.setFill(color_rgb(255, 255, 0))
  sbox.draw(win)

  cx = 500
  cx1 = 475
  crosshair = Rectangle(Point(cx, 500), Point(cx1, 525))
  crosshair.setFill(color_rgb(0, 0, 255))
  crosshair.draw(win)

  win.getKey()
  cx += 1

  while True:

      if cx < 700 or cx1 < 700:
          crosshair.move(cx, 0)
          crosshair.move(cx1, 0)
      elif cx > 100 or cx1 > 100:
          crosshair.move(cx, 0)
          crosshair.move(cx1, 0)
      else:
          cx += 0
          break
