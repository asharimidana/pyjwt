class Contoh:
    def a(self):
        # print("ini dari method a")
        python tak bisa memanggil fungsi yang blm dipanggil
        print(self.b)

    def b(self):
        print("ini adalah = ")


ax = Contoh()
ax.a()
