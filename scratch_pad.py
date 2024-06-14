def foo(songs):
    mapp = {}
    for song in songs:
        mapp[song] = 1

    for key in mapp:
        print(key)

foo([40,50,10,80,90])