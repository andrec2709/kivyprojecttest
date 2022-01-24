from kivy_deps import sdl2

coll = COLLECT(exe, Tree('C:\\Users\\ANDRE\\PycharmProjects\\kivyprojecttest\\'),
               a.binaries,
               a.zipfiles,
               a.datas,
               *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
               strip=False,
               upx=True,
               name="kivyprojecttest"
)