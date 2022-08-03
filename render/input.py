# checking inputs
if camera.movement_enabled:
    # movement input
    keys = pygame.key.get_pressed()
    move_dir = Vector2()
    if keys[pygame.K_w]:
        move_dir += Vector2(0, 1)
    if keys[pygame.K_a]:
        move_dir += Vector2(-1, 0)
    if keys[pygame.K_s]:
        move_dir += Vector2(0, -1)
    if keys[pygame.K_d]:
        move_dir += Vector2(1, 0)

    # calculating camera velocity
    speed = camera.movespeed
    new_vel = Vector2()
    if move_dir.magnitude > 0:
        new_vel = move_dir.unit * speed

    new_vel /= camera.zoom

    # rotation input
    rotate_dir = 0
    if keys[pygame.K_q]:
        rotate_dir += 1
    if keys[pygame.K_e]:
        rotate_dir -= 1

    # calculating rotation velocity
    rotate_vel = (rotate_dir * camera.rotatespeed)

    # zoom input
    zoom_rate = 0
    if keys[pygame.K_i]:
        zoom_rate += camera.zoomspeed
    if keys[pygame.K_o]:
        zoom_rate -= camera.zoomspeed

    # adjusting camera cframe
    camera.cframe = camera.cframe * CFrame(new_vel*dt) * CFrame.angle(rotate_vel*dt)
    camera.zoom = max(min(camera.zoom + zoom_rate*dt, camera.zoom_max), camera.zoom_min)

    # resetting camera rotation
    if keys[pygame.K_r]:
        camera.cframe = CFrame(camera.cframe.p)