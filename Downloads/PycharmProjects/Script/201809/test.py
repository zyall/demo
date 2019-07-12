# class Game():
#     def __init__(self):
#         self.lines = []
#         self.getenter()
#         self.getlist()
#
#     def getenter(self):
#         while True:
#             s = input("")
#             if s:
#                 self.lines.append(s)
#             else:
#                 break
#         Game.lines = self.lines
#         return Game.lines
#
#     def getlist(self):
#         l = []
#         for i in Game.lines:
#             i = i.split()
#             l.append(i)
#         Game.l = l
#         return Game.l
#
#     def getresult(self):
#         t = [0, 0]
#         for i in range(len(Game.l)):
#             for j in range(1):
#                 key = Game.l[i][j]
#                 value = int(Game.l[i][j + 1])
#                 if key == 'UP':
#                     t[0] += value
#                 elif key == 'LEFT':
#                     t[1] -= value
#                 elif key == 'DOWN':
#                     t[0] -= value
#                 elif key == 'RIGHT':
#                     t[1] += value
#         return tuple(t)
# #
# if __name__ == '__main__':
#     c = Game()
#     print(c.getresult())









