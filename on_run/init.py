# creating football field lines
width = 85
length = 160
points = [Vector2(-length/2, -width/2), Vector2(-length/2, width/2), Vector2(length/2, width/2), Vector2(length/2, -width/2), Vector2(-length/2, -width/2)]

alt_bool = True
for i in range(8, length, 8):
    line_pos = i - length/2
    if alt_bool:
        points.append(Vector2(line_pos, -width/2))
        points.append(Vector2(line_pos, width/2))
    else:
        points.append(Vector2(line_pos, width/2))
        points.append(Vector2(line_pos, -width/2))

    alt_bool = not alt_bool

lines = Line(points, surface=screen, width=15, color=(255, 255, 255))

# 50
line50_1 = ImageRect("50.png", surface=screen)
line50_1.cframe = CFrame(0, width*2)
line50_1.size = Vector2(50, 50)
line50_2 = ImageRect("50.png", surface=screen)
line50_2.cframe = CFrame(0, -width*2)
line50_2.size = Vector2(50, 50)

# 40
line40l_1 = ImageRect("40.png", surface=screen)
line40l_1.cframe = CFrame(-80, -width*2)
line40l_1.size = Vector2(50, 50)
line40l_2 = ImageRect("40.png", surface=screen)
line40l_2.cframe = CFrame(-80, width*2)
line40l_2.size = Vector2(50, 50)

line40r_1 = ImageRect("40.png", surface=screen)
line40r_1.cframe = CFrame(80, -width*2)
line40r_1.size = Vector2(50, 50)
line40r_2 = ImageRect("40.png", surface=screen)
line40r_2.cframe = CFrame(80, width*2)
line40r_2.size = Vector2(50, 50)

# 30
line30l_1 = ImageRect("30.png", surface=screen)
line30l_1.cframe = CFrame(-160, -width*2)
line30l_1.size = Vector2(50, 50)
line30l_2 = ImageRect("30.png", surface=screen)
line30l_2.cframe = CFrame(-160, width*2)
line30l_2.size = Vector2(50, 50)

line30r_1 = ImageRect("30.png", surface=screen)
line30r_1.cframe = CFrame(160, -width*2)
line30r_1.size = Vector2(50, 50)
line30r_2 = ImageRect("30.png", surface=screen)
line30r_2.cframe = CFrame(160, width*2)
line30r_2.size = Vector2(50, 50)

# 20
line20l_1 = ImageRect("20.png", surface=screen)
line20l_1.cframe = CFrame(-240, -width*2)
line20l_1.size = Vector2(50, 50)
line20l_2 = ImageRect("20.png", surface=screen)
line20l_2.cframe = CFrame(-240, width*2)
line20l_2.size = Vector2(50, 50)

line20r_1 = ImageRect("20.png", surface=screen)
line20r_1.cframe = CFrame(240, -width*2)
line20r_1.size = Vector2(50, 50)
line20r_2 = ImageRect("20.png", surface=screen)
line20r_2.cframe = CFrame(240, width*2)
line20r_2.size = Vector2(50, 50)

# 10
line10l_1 = ImageRect("10.png", surface=screen)
line10l_1.cframe = CFrame(-320, -width*2)
line10l_1.size = Vector2(50, 50)
line10l_2 = ImageRect("10.png", surface=screen)
line10l_2.cframe = CFrame(-320, width*2)
line10l_2.size = Vector2(50, 50)

line10r_1 = ImageRect("10.png", surface=screen)
line10r_1.cframe = CFrame(320, -width*2)
line10r_1.size = Vector2(50, 50)
line10r_2 = ImageRect("10.png", surface=screen)
line10r_2.cframe = CFrame(320, width*2)
line10r_2.size = Vector2(50, 50)

# creating metronome
metronome = Metronome(120)

# creating band members
squad = Squad(screen, metronome, CFrame(-7*5, -5*width/2 - 8*5) * CFrame.angle(math.pi/2))

# save your tears
squad.mark_time(8)
squad.forward_march(8)
squad.forward_march(16)
squad.mark_time(8)
squad.left_pinwheel(8)
squad.right_face(); squad.forward_march(8)
squad.mark_time(8)
squad.forward_march(8)
squad.right_face(); squad.left_pinwheel(8)
squad.turn_right(180, 4); squad.mark_time(2)
squad.mark_time(32 + 2)

# take my breath
squad.mark_time(4)
squad.forward_march(4); squad.mark_time(4)
squad.left_slant()
squad.mark_time(16)
squad.right_face(); squad.forward_march(8)
squad.right_face(); squad.forward_march(8)
squad.left_face(); squad.left_slant()
squad.turn_right(180, 4); squad.mark_time(4)
squad.right_pinwheel(8)
squad.forward_march(8)
squad.mark_time(16)

# can't feel my face
squad.mark_time(4)
squad.left_slant()
squad.right_face(), squad.forward_march(8)
squad.left_face(); squad.mark_time(16)
squad.left_face(); squad.forward_march(8)
squad.right_face(); squad.mark_time(24)
squad.mark_time(16)

# guard feature
metronome.tempo = 57
squad.mark_time(16)

metronome.tempo = 115
squad.mark_time(288)

# dance mix
metronome.tempo = 95
squad.right_slant()
squad.forward_march(8)
squad.mark_time(16)
squad.mark_time(8) # stagger first 4
squad.mark_time(12)

metronome.tempo = 98
squad.mark_time(8) # body rolls
squad.turn_right(360, 8) # cross
squad.mark_time(8) # lrlk rlrk
squad.mark_time(8) # lrll rlrr
squad.mark_time(8) # dips
squad.turn_right(360, 8) # spin
squad.mark_time(8) # rainbow
squad.mark_time(8)

squad.mark_time(4) # chant
squad.mark_time(8) # ptp, cc, twirl
squad.mark_time(8) # push, boogie, throw
squad.mark_time(8) # up up surf surf down up push
squad.mark_time(4) # horn up

metronome.tempo = 110
squad.mark_time(8) # splits
squad.mark_time(8) # bow
squad.mark_time(8) # unstagger
squad.mark_time(32) # waiting for cue
squad.forward_march(32) # off the field
squad.mark_time(8)