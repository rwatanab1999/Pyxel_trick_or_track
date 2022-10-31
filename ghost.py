from cmath import pi
import math
import random
import pyxel
import webbrowser

SCENE_TITLE = 0
SCENE_PLAY = 1

endroll_x = 160


class Boy:
    def __init__(self, x, y, d, status):
        self.x = x
        self.y = y
        self.d = d
        self.status = status


class Ghost:
    def __init__(self, x, y, d, status):
        self.x = x
        self.y = y
        self.d = d
        self.status = status


class Pumpkin:
    def __init__(self, x, y, d, status):
        self.x = x
        self.y = y
        self.d = d
        self.status = status


class Satan:
    def __init__(self, x, y, d, status):
        self.x = x
        self.y = y
        self.d = d
        self.status = status


class Skeleton:
    def __init__(self, x, y, d, status):
        self.x = x
        self.y = y
        self.d = d
        self.status = status


class Candy:
    def __init__(self, x, y, count):
        self.x = x
        self.y = y
        self.count = count


class App:
    def __init__(self):
        pyxel.init(160, 208, title="Happy Helloween", fps = 36)
        pyxel.load("ghost_ast.pyxres")
        self.scene = SCENE_TITLE

        self.boy = Boy(72, 28, 3, 1)
        self.ghost = Ghost(-20, 128, 0, 0)
        self.pumpkin = Pumpkin(-20, 15, 0, 0)
        self.satan = Satan(-20, 40, 0, 0)
        self.skeleton = Skeleton(-20, 80, 0, 0)
        self.candy = Candy(80, 64, 0)

        pyxel.run(self.update, self.draw)

    def update_boy_move(self):

        if self.boy.status == 1:
            if abs(self.ghost.x - self.boy.x) < 8 and abs(self.ghost.y - self.boy.y) < 8:
                self.boy.status = 0
            if abs(self.pumpkin.x - self.boy.x) < 8 and abs(self.pumpkin.y - self.boy.y) < 8:
                self.boy.status = 0
            if abs(self.satan.x - self.boy.x) < 8 and abs(self.satan.y - self.boy.y) < 8:
                self.boy.status = 0
            if abs(self.skeleton.x - self.boy.x) < 8 and abs(self.skeleton.y - self.boy.y) < 8:
                self.boy.status = 0
            if (pyxel.btnp(pyxel.KEY_LEFT, 1, 1) or \
                    ((56 <= pyxel.mouse_x <= 72) and (144 <= pyxel.mouse_y <= 192) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)))\
                        and self.boy.x > 3:  # 左移動
                self.boy.x -= 2
                self.boy.d = 1
            elif (pyxel.btnp(pyxel.KEY_RIGHT, 1, 1) or \
                    ((88 <= pyxel.mouse_x <= 104) and (144 <= pyxel.mouse_y <= 192) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)))\
                        and self.boy.x < 141:  # 右移動
                self.boy.x += 2
                self.boy.d = 0
            if (pyxel.btnp(pyxel.KEY_UP, 1, 1) or \
                    ((56 <= pyxel.mouse_x <= 104) and (144 <= pyxel.mouse_y <= 160) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)))\
                        and self.boy.y > 20:  # 上移動
                self.boy.y -= 2
                self.boy.d = 2
            elif (pyxel.btnp(pyxel.KEY_DOWN, 1, 1) or \
                    ((56 <= pyxel.mouse_x <= 104) and (176 <= pyxel.mouse_y <= 192) and pyxel.btn(pyxel.MOUSE_BUTTON_LEFT)))\
                        and self.boy.y < 113:  # 下移動
                self.boy.y += 2
                self.boy.d = 3

    def update_ghost_move(self):
        if (self.ghost.x > self.boy.x) and (self.ghost.y == self.boy.y):  # 左移動
            self.ghost.x -= 0.6
            self.ghost.d = 2
        elif (self.ghost.x < self.boy.x) and (self.ghost.y == self.boy.y):  # 右移動
            self.ghost.x += 0.6
            self.ghost.d = 0
        if (self.ghost.y > self.boy.y) and (self.ghost.x == self.boy.x):  # 下移動
            self.ghost.y -= 0.6
            self.ghost.d = 3
        elif (self.ghost.y < self.boy.y) and (self.ghost.x == self.boy.x):  # 上移動
            self.ghost.y += 0.6
            self.ghost.d = 1
        if (self.ghost.x > self.boy.x) and (self.ghost.y > self.boy.y):  # 左上移動
            self.ghost.x -= 0.4
            self.ghost.y -= 0.4
            self.ghost.d = 3
        elif (self.ghost.x < self.boy.x) and (self.ghost.y < self.boy.y):  # 右下移動
            self.ghost.x += 0.4
            self.ghost.y += 0.4
            self.ghost.d = 1
        if (self.ghost.x < self.boy.x) and (self.ghost.y > self.boy.y):  # 右上移動
            self.ghost.x += 0.4
            self.ghost.y -= 0.4
            self.ghost.d = 1
        elif (self.ghost.x > self.boy.x) and (self.ghost.y < self.boy.y):  # 左下移動
            self.ghost.x -= 0.4
            self.ghost.y += 0.4
            self.ghost.d = 3

    def update_pumpkin_move(self):
        if (self.pumpkin.x > self.boy.x) and (self.pumpkin.y == self.boy.y):  # 左移動
            self.pumpkin.x -= 0.6
            self.pumpkin.d = 2
        elif (self.pumpkin.x < self.boy.x) and (self.pumpkin.y == self.boy.y):  # 右移動
            self.pumpkin.x += 0.6
            self.pumpkin.d = 0
        if (self.pumpkin.y > self.boy.y) and (self.pumpkin.x == self.boy.x):  # 下移動
            self.pumpkin.y -= 0.6
            self.pumpkin.d = 3
        elif (self.pumpkin.y < self.boy.y) and (self.pumpkin.x == self.boy.x):  # 上移動
            self.pumpkin.y += 0.6
            self.pumpkin.d = 1
        if (self.pumpkin.x > self.boy.x) and (self.pumpkin.y > self.boy.y):  # 左上移動
            self.pumpkin.x -= 0.8
            self.pumpkin.y -= 0.3
            self.pumpkin.d = 1
        elif (self.pumpkin.x < self.boy.x) and (self.pumpkin.y < self.boy.y):  # 右下移動
            self.pumpkin.x += 0.8
            self.pumpkin.y += 0.3
            self.pumpkin.d = 3
        if (self.pumpkin.x < self.boy.x) and (self.pumpkin.y > self.boy.y):  # 右上移動
            self.pumpkin.x += 0.8
            self.pumpkin.y -= 0.3
            self.pumpkin.d = 0
        elif (self.pumpkin.x > self.boy.x) and (self.pumpkin.y < self.boy.y):  # 左下移動
            self.pumpkin.x -= 0.8
            self.pumpkin.y += 0.3
            self.pumpkin.d = 3

    def update_satan_move(self):
        if (self.satan.x > self.boy.x) and (self.satan.y == self.boy.y):  # 左移動
            self.satan.x -= 0.5 + 0.6 * \
                math.sin(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.d = 2
        elif (self.satan.x < self.boy.x) and (self.satan.y == self.boy.y):  # 右移動
            self.satan.x += 0.5 + 0.6 * \
                math.sin(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.d = 0
        if (self.satan.y > self.boy.y) and (self.satan.x == self.boy.x):  # 下移動
            self.satan.y -= 0.5 + 0.6 * \
                math.cos(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.d = 3
        elif (self.satan.y < self.boy.y) and (self.satan.x == self.boy.x):  # 上移動
            self.satan.y += 0.5 + 0.6 * \
                math.cos(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.d = 1
        if (self.satan.x > self.boy.x) and (self.satan.y > self.boy.y):  # 左上移動
            self.satan.x -= 0.8 + \
                math.sin(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.y -= 0.8 + \
                math.cos(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.d = 3
        elif (self.satan.x < self.boy.x) and (self.satan.y < self.boy.y):  # 右下移動
            self.satan.x += 0.8 + \
                math.sin(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.y += 0.8 + \
                math.cos(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.d = 1
        if (self.satan.x < self.boy.x) and (self.satan.y > self.boy.y):  # 右上移動
            self.satan.x += 0.8 + \
                math.sin(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.y -= 0.8 + \
                math.cos(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.d = 1
        elif (self.satan.x > self.boy.x) and (self.satan.y < self.boy.y):  # 左下移動
            self.satan.x -= 0.8 + \
                math.sin(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.y += 0.8 + \
                math.cos(2*math.pi*(pyxel.frame_count % 30)/30)
            self.satan.d = 3

    def update_skeleton_move(self):
        if (self.skeleton.x > self.boy.x) and (self.skeleton.y == self.boy.y):  # 左移動
            self.skeleton.x -= 1
            self.skeleton.d = 1
        elif (self.skeleton.x < self.boy.x) and (self.skeleton.y == self.boy.y):  # 右移動
            self.skeleton.x += 1
            self.skeleton.d = 0
        if (self.skeleton.y > self.boy.y) and (self.skeleton.x == self.boy.x):  # 下移動
            self.skeleton.y -= 1
            self.skeleton.d = 3
        elif (self.skeleton.y < self.boy.y) and (self.skeleton.x == self.boy.x):  # 上移動
            self.skeleton.y += 1
            self.skeleton.d = 2
        if (self.skeleton.x > self.boy.x) and (self.skeleton.y > self.boy.y):  # 左上移動
            self.skeleton.x -= 0.7 + \
                math.sin(1.5 * pi * (pyxel.frame_count % 20) / 20)
            self.skeleton.y -= 0.4 + \
                math.cos(1.5 * pi * (pyxel.frame_count % 20) / 20)
            self.skeleton.d = 1
        elif (self.skeleton.x < self.boy.x) and (self.skeleton.y < self.boy.y):  # 右下移動
            self.skeleton.x += 0.7 + \
                math.cos(1.5 * pi * (pyxel.frame_count % 20) / 20)
            self.skeleton.y += 0.4 + \
                math.sin(0.2 * pi * (pyxel.frame_count % 20) / 20)
            self.skeleton.d = 3
        if (self.skeleton.x < self.boy.x) and (self.skeleton.y > self.boy.y):  # 右上移動
            self.skeleton.x += 0.7 + \
                math.sin(1.5 * pi * (pyxel.frame_count % 20) / 20)
            self.skeleton.y -= 0.4 + \
                math.cos(1.5 * pi * (pyxel.frame_count % 20) / 20)
            self.skeleton.d = 0
        elif (self.skeleton.x > self.boy.x) and (self.skeleton.y < self.boy.y):  # 左下移動
            self.skeleton.x -= 0.7 + \
                math.cos(1.5 * pi * (pyxel.frame_count % 20) / 20)
            self.skeleton.y += 0.4 + \
                math.sin(0.2 * pi * (pyxel.frame_count % 20) / 20)
            self.skeleton.d = 3

    def update_candy_status(self):
        if abs(self.candy.x - self.boy.x) < 8 and abs(self.candy.y - self.boy.y) < 8:
            self.candy.count += 1
            self.candy.x = random.randint(3, 141)
            self.candy.y = random.randint(20, 113)

    def update(self):

        self.update_boy_move()
        if (self.candy.count >= 3):
            if self.ghost.status == 0:
                self.ghost = Ghost(24, 56, 0, 1)
            self.update_ghost_move()
        if (self.candy.count >= 16):
            if self.pumpkin.status == 0:
                self.pumpkin = Pumpkin(56, 56, 0, 1)
            self.update_pumpkin_move()
        if (self.candy.count >= 29):
            if self.skeleton.status == 0:
                self.skeleton = Skeleton(88, 56, 0, 1)
            self.update_skeleton_move()
        if (self.candy.count >= 42):
            if self.satan.status == 0:
                self.satan = Satan(120, 56, 0, 1)
            self.update_satan_move()
        self.update_candy_status()
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw_title_scene(self):
        pyxel.bltm(0, 0, 1, 0, 0, 160, 96, 0)
        pyxel.blt(72, 144, 1, 16, 208, 16, 16, 0) #up
        pyxel.blt(72, 160, 1, 16, 224, 16, 16, 0) #mid
        pyxel.blt(72, 176, 1, 16, 240, 16, 16, 0) #down

        pyxel.blt(56, 144, 1, 0, 208, 16, 16, 0) #left_up
        pyxel.blt(88, 144, 1, 32, 208, 16, 16, 0) #right_up

        pyxel.blt(56, 160, 1, 0, 224, 16, 16, 0) #left
        pyxel.blt(88, 160, 1, 32, 224, 16, 16, 0) #right

        pyxel.blt(56, 176, 1, 0, 240, 16, 16, 0) #left_down
        pyxel.blt(88, 176, 1, 32, 240, 16, 16, 0) #right_down

        pyxel.blt((pyxel.frame_count) % (pyxel.width + 100), 76, 0, 0, 16 + 16 * (pyxel.frame_count % 4), 16, 16, 10)
        pyxel.blt((pyxel.frame_count - 48) % (pyxel.width + 100), 76, 0, 0, 0, 16, 16, 10)
        pyxel.blt((pyxel.frame_count - 64) % (pyxel.width + 100), 76, 0, 0, 16*6 + 16 * (pyxel.frame_count % 4), 16, 16, 10)
        pyxel.blt((pyxel.frame_count - 80) % (pyxel.width + 100), 76, 0, 0, 16*11 + 16 * (pyxel.frame_count % 4), 16, 16, 10)
        pyxel.blt((pyxel.frame_count - 96) % (pyxel.width + 100), 76, 0, 0, 160, 16, 16, 10)

        pyxel.text(67, 98, "> PLAY", 7)

        # shere tweet
        pyxel.blt(2, 108, 2, 80, 0, 16, 16, 0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (2 <= pyxel.mouse_x <= 18) and (108 <= pyxel.mouse_y <= 124):
            webbrowser.open("https://twitter.com/intent/tweet?text=TRICK%20OR%20TRACK%20!%0A%0A%E5%90%9B%E3%81%AF%E3%81%A9%E3%82%8C%E3%81%A0%E3%81%91%E3%81%8A%E8%8F%93%E5%AD%90%E3%82%92%E3%82%B2%E3%83%83%E3%83%88%E5%87%BA%E6%9D%A5%E3%82%8B%E3%81%8B%E3%81%AA%20%3F%0A%E2%86%93%E3%83%AA%E3%83%B3%E3%82%AF%E5%85%88%E3%81%8B%E3%82%89%E3%83%AF%E3%83%B3%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E3%81%A7%E9%81%8A%E3%81%B9%E3%82%8B%E3%82%88%0A%E3%80%90PLAY%E3%80%91https%3A%2F%2Fkitao.github.io%2Fpyxel%2Fwasm%2Flauncher%2F%3Fplay%3Drwatanab1999.Pyxel_trick_or_track.trick_or_track%0A%0A%E5%88%B6%E4%BD%9C%E8%80%85%20%3A%20%40chang_code%0A%23TRICK_OR_TRACK%20%2342Tokyo%20%23Pyxel%0Ahttps%3A%2F%2Ftwitter.com%2Fchang_code%2Fstatus%2F1586946127911583744")
        # twitter link
        pyxel.blt(21, 108, 2, 16, 0, 16, 16, 0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (21 <= pyxel.mouse_x <= 37) and (108 <= pyxel.mouse_y <= 124):
            webbrowser.open("https://twitter.com/chang_code")

        pyxel.text(43, 113, "2022 (c)chang_code", 7)

        # github link
        pyxel.blt(120, 108, 2, 32, 0, 16, 16, 0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (120 <= pyxel.mouse_x <= 136) and (108 <= pyxel.mouse_y <= 124):
            webbrowser.open("https://github.com/rwatanab1999/Pyxel_Game")

        # 42Tokyo link
        pyxel.blt(140, 108, 2, 48, 0, 16, 16, 0)
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (140 <= pyxel.mouse_x <= 156) and (108 <= pyxel.mouse_y <= 124):
            webbrowser.open("https://42tokyo.jp")

        # mouse icon
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 2, 64, 0, 16, 16, 0)
        
        #ENTERでゲーム画面に遷移
        if pyxel.btnp(pyxel.KEY_RETURN) or (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (67 <= pyxel.mouse_x <= 99) and (90 <= pyxel.mouse_y <= 106)):
            self.scene = SCENE_PLAY

    def draw_play_scene(self):
        pyxel.cls(0)
        pyxel.bltm(0, 16, 0, 0, 0, 160, 96, 0)
        pyxel.blt(72, 144, 1, 16, 208, 16, 16, 0) #up
        pyxel.blt(72, 160, 1, 16, 224, 16, 16, 0) #mid
        pyxel.blt(72, 176, 1, 16, 240, 16, 16, 0) #down

        pyxel.blt(56, 144, 1, 0, 208, 16, 16, 0) #left_up
        pyxel.blt(88, 144, 1, 32, 208, 16, 16, 0) #right_up

        pyxel.blt(56, 160, 1, 0, 224, 16, 16, 0) #left
        pyxel.blt(88, 160, 1, 32, 224, 16, 16, 0) #right

        pyxel.blt(56, 176, 1, 0, 240, 16, 16, 0) #left_down
        pyxel.blt(88, 176, 1, 32, 240, 16, 16, 0) #right_down

        if self.ghost.status == 0:
            pyxel.blt(24, 56, 1, 0, 96, 16, 16, 0)
        if self.pumpkin.status == 0:
            pyxel.blt(56, 56, 1, 16, 96, 16, 16, 0)
        if self.skeleton.status == 0:
            pyxel.blt(88, 56, 1, 32, 96, 16, 16, 0)
        if self.satan.status == 0:
            pyxel.blt(120, 56, 1, 48, 96, 16, 16, 0)

        if self.boy.status == 0:
            global endroll_x
            endroll_x += -1
            if endroll_x > -240:
                if endroll_x > -30:
                    pyxel.blt(self.boy.x - 5, self.boy.y, 1, 16 * (int)((pyxel.frame_count % 16)/4), 128, 16, 16, 0)
                    pyxel.blt(self.boy.x + 5, self.boy.y, 1, 16 * (int)((pyxel.frame_count % 16)/4), 128, -16, 16, 0)
                else :
                    pyxel.blt(72, 68, 1, 32, 16, 16, 16, 0) 
                pyxel.bltm(endroll_x, 32, 1, 0, 120, 240, 81, 10)
            else :
                # 自分のお墓
                pyxel.blt(72, 68, 1, 32, 16, 16, 16, 0)
                # twiter 
                pyxel.blt(143, 1, 2, 16, 0, 16, 16, 0)
                pyxel.text(90, 6, "SHERE SCORE >", 7)
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (143 <= pyxel.mouse_x <= 159) and (1 <= pyxel.mouse_y <= 17):
                    template_link = "https://twitter.com/intent/tweet?text=TRICK%20OR%20TRACK%20!%0A%0A%E3%81%8A%E8%8F%93%E5%AD%90%E3%82%92%E3%80%8E%20{}%20%E5%80%8B%20%E3%80%8F%E3%82%B2%E3%83%83%E3%83%88%E5%87%BA%E6%9D%A5%E3%81%9F%E3%81%AE%E3%81%A0%20!%0A%E2%86%93%E3%83%AA%E3%83%B3%E3%82%AF%E5%85%88%E3%81%8B%E3%82%89%E3%83%AF%E3%83%B3%E3%82%AF%E3%83%AA%E3%83%83%E3%82%AF%E3%81%A7%E9%81%8A%E3%81%B9%E3%82%8B%E3%82%88%0A%E3%80%90PLAY%E3%80%91https%3A%2F%2Fkitao.github.io%2Fpyxel%2Fwasm%2Flauncher%2F%3Fplay%3Drwatanab1999.Pyxel_trick_or_track.trick_or_track%0A%0A%E5%88%B6%E4%BD%9C%E8%80%85%20%3A%20%40chang_code%0A%23TRICK_OR_TRACK%20%2342Tokyo%20%23Pyxel%0Ahttps%3A%2F%2Ftwitter.com%2Fchang_code%2Fstatus%2F1586946127911583744"
                    word_score = self.candy.count
                    form_link = template_link.format(word_score)
                    webbrowser.open(form_link)

                # retry button
                pyxel.text(67, 98, "> RETRY", 7)
                if pyxel.btnp(pyxel.KEY_RETURN) or (pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (67 <= pyxel.mouse_x <= 99) and (90 <= pyxel.mouse_y <= 106)):
                    self.scene = SCENE_TITLE
                    endroll_x = 160
                    self.boy = Boy(72, 28, 3, 1)
                    self.ghost = Ghost(-20, 128, 0, 0)
                    self.pumpkin = Pumpkin(-20, 15, 0, 0)
                    self.satan = Satan(-20, 40, 0, 0)
                    self.skeleton = Skeleton(-20, 80, 0, 0)
                    self.candy = Candy(80, 64, 0)

        text_score = "SCORE:{}"
        word_count = self.candy.count
        text_candy = text_score.format(word_count)
        pyxel.text(5, 6, text_candy, 8)

        if self.boy.status == 1:
            pyxel.blt(self.candy.x, self.candy.y, 0, 16 *
                    (self.candy.count % 8), 80, 16, 16, 0)
            pyxel.blt(self.boy.x, self.boy.y, 0, 16 * self.boy.d,
                    16 + 16 * (pyxel.frame_count % 4), 16, 16, 10)
            pyxel.blt(self.ghost.x, self.ghost.y, 0,
                    16 * self.ghost.d, 0, 16, 16, 10)
            pyxel.blt(self.satan.x, self.satan.y, 0,
                    16 * self.satan.d, 160, 16, 16, 10)
            pyxel.blt(self.pumpkin.x, self.pumpkin.y, 0, 16 * self.pumpkin.d,
                    96 + 16 * (pyxel.frame_count % 4), 16, 16, 10)
            pyxel.blt(self.skeleton.x, self.skeleton.y, 0, 16 *
                    self.skeleton.d, 176 + 16 * (pyxel.frame_count % 4), 16, 16, 10)
        pyxel.bltm(0, 112, 0, 0, 96, 160, 16, 0)

        # mouse icon
        pyxel.blt(pyxel.mouse_x, pyxel.mouse_y, 2, 64, 0, 16, 16, 0)

    def draw(self):
        # 画面クリア 0は黒
        pyxel.cls(0)

        #描画の画面分岐
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()

App()
