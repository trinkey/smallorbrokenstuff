# setup
import turtle
import random
s1 = turtle.Screen()
s1.tracer(0)
s1.setup(500,500);
s1.bgcolor(0,0,0);
t1 = turtle.Turtle()
t1.hideturtle();
t1.penup();
t1.shape("turtle");
t1.speed(100);
cx = -250

# starting color (by tens, 0 - 250, one number has to be 250 and one has to be 0)
if random.randint(0,2) == 0:
  if random.randint(0,1) == 0:
    cr_0 = random.randint(0,25) * 10
    cg_0 = 250
    cb_0 = 0
  else:
    cr_0 = 250
    cg_0 = random.randint(0,25) * 10
    cb_0 = 0
elif random.randint(0,1) == 0:
  if random.randint(0,1) == 0:
    cg_0 = random.randint(0,25) * 10
    cb_0 = 250
    cr_0 = 0
  else:
    cg_0 = 250
    cb_0 = random.randint(0,25) * 10
    cr_0 = 0
else:
  if random.randint(0,1) == 0:
    cb_0 = random.randint(0,25) * 10
    cr_0 = 250
    cg_0 = 0
  else:
    cb_0 = 250
    cr_0 = random.randint(0,25) * 10
    cg_0 = 0

for i in range(50):
  t1.goto(cx,250)
  cr = cr_0
  cg = cg_0
  cb = cb_0
  cy = 250
  for i in range(50):
    if cr == 0:
      if cg == 0:
        cr = 10
      elif cg == 250:
        if cb != 250:
          cb = cb + 10
        elif cb == 250:
          if cg != 0:
            cg = cg - 10
          else:
            cr = cr + 10
      elif cg > 0 and cg < 250:
        if cb == 250:
          cg = cg - 10
        elif cb != 250:
          cg = cg + 10
    elif cr != 250:
      if cb == 250:
        cr = cr + 10
      elif cg == 250:
        cr = cr - 10
    elif cr == 250:
      if cb != 0:
        cb = cb - 10
      elif cg != 0:
        if cg != 250:
          cg = cg + 10
        elif cg == 250:
          cr = cr - 10
      elif cg == 0:
        cg = 10
    t1.color(cr,cg,cb);
    t1.goto(cx,cy);
    t1.stamp();
    cy = cy - 10
  if cr_0 == 0:
    if cg_0 == 0:
      cr_0 = 10
    elif cg_0 == 250:
      if cb_0 != 250:
        cb_0 = cb_0 + 10
      elif cb_0 == 250:
        if cg_0 != 0:
          cg_0 = cg_0 - 10
        else:
          cr_0 = cr_0 + 10
    elif cg_0 > 0 and cg_0 < 250:
      if cb_0 == 250:
        cg_0 = cg_0 - 10
      elif cb_0 != 250:
        cg_0 = cg_0 + 10
  elif cr_0 != 250:
    if cb_0 == 250:
      cr_0 = cr_0 + 10
    elif cg_0 == 250:
      cr_0 = cr_0 - 10
  elif cr_0 == 250:
    if cb_0 != 0:
      cb_0 = cb_0 - 10
    elif cg_0 != 0:
      if cg_0 != 250:
        cg_0 = cg_0 + 10
      elif cg_0 == 250:
        cr_0 = cr_0 - 10
    elif cg_0 == 0:
       cg_0 = 10
  cx = cx + 10
t1.hideturtle()
s1.update()
