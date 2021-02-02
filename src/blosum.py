blosum = {
        'a': {'a':  4,'r': -1,'n': -2,'d': -2,'c':  0,'q': -1,'e': -1,'g':  0,'h': -2,'i': -1,'l': -1,'k': -1,'m': -1,'f': -2,'p': -1,'s': 1,'t': 0,'w': -3,'y': -2,'v': 0,'b': -2,'z': -1,'x': 0},
        'r': {'a': -1,'r':  5,'n':  0,'d': -2,'c': -3,'q':  1,'e':  0,'g': -2,'h':  0,'i': -3,'l': -2,'k': 2,'m': -1,'f': -3,'p': -2,'s': -1,'t': -1,'w': -3,'y': -2,'v': -3,'b': -1,'z': 0,'x': -1},
        'n': {'a': -2,'r':  0,'n':  6,'d':  1,'c': -3,'q':  0,'e':  0,'g':  0,'h':  1,'i': -3,'l': -3,'k': 0,'m': -2,'f': -3,'p': -2,'s': 1,'t': 0,'w': -4,'y': -2,'v': -3,'b': 3,'z': 0,'x': -1},
        'd': {'a': -2,'r': -2,'n':  1,'d':  6,'c': -3,'q':  0,'e':  2,'g': -1,'h': -1,'i': -3,'l': -4,'k': -1,'m': -3,'f': -3,'p': -1,'s': 0,'t': -1,'w': -4,'y': -3,'v': -3,'b': 4,'z': 1,'x': -1},
        'c': {'a':  0,'r': -3,'n': -3,'d': -3,'c':  9,'q': -3,'e': -4,'g': -3,'h': -3,'i': -1,'l': -1,'k': -3,'m': -1,'f': -2,'p': -3,'s': -1,'t': -1,'w': -2,'y': -2,'v': -1,'b': -3,'z': -3,'x': -2},
        'q': {'a': -1,'r':  1,'n':  0,'d':  0,'c': -3,'q':  5,'e':  2,'g': -2,'h':  0,'i': -3,'l': -2,'k': 1,'m': 0,'f': -3,'p': -1,'s': 0,'t': -1,'w': -2,'y': -1,'v': -2,'b': 0,'z': 3,'x': -1},
        'e': {'a': -1,'r':  0,'n':  0,'d':  2,'c': -4,'q':  2,'e':  5,'g': -2,'h':  0,'i': -3,'l': -3,'k': 1,'m': -2,'f': -3,'p': -1,'s': 0,'t': -1,'w': -3,'y': -2,'v': -2,'b': 1,'z': 4,'x': -1},
        'g': {'a':  0,'r': -2,'n':  0,'d': -1,'c': -3,'q': -2,'e': -2,'g':  6,'h': -2,'i': -4,'l': -4,'k': -2,'m': -3,'f': -3,'p': -2,'s': 0,'t': -2,'w': -2,'y': -3,'v': -3,'b': -1,'z': -2,'x': -1},
        'h': {'a': -2,'r':  0,'n':  1,'d': -1,'c': -3,'q':  0,'e':  0,'g': -2,'h':  8,'i': -3,'l': -3,'k': -1,'m': -2,'f': -1,'p': -2,'s': -1,'t': -2,'w': -2,'y': 2,'v': -3,'b': 0,'z': 0,'x': -1},
        'i': {'a': -1,'r': -3,'n': -3,'d': -3,'c': -1,'q': -3,'e': -3,'g': -4,'h': -3,'i':  4,'l': 2,'k': -3,'m': 1,'f': 0,'p': -3,'s': -2,'t': -1,'w': -3,'y': -1,'v': 3,'b': -3,'z': -3,'x': -1},
        'l': {'a': -1,'r': -2,'n': -3,'d': -4,'c': -1,'q': -2,'e': -3,'g': -4,'h': -3,'i':  2,'l': 4,'k': -2,'m': 2,'f': 0,'p': -3,'s': -2,'t': -1,'w': -2,'y': -1,'v': 1,'b': -4,'z': -3,'x': -1},
        'k': {'a': -1,'r':  2,'n':  0,'d': -1,'c': -3,'q':  1,'e':  1,'g': -2,'h': -1,'i': -3,'l': -2,'k': 5,'m': -1,'f': -3,'p': -1,'s': 0,'t': -1,'w': -3,'y': -2,'v': -2,'b': 0,'z': 1,'x': -1},
        'm': {'a': -1,'r': -1,'n': -2,'d': -3,'c': -1,'q':  0,'e': -2,'g': -3,'h': -2,'i':  1,'l': 2,'k': -1,'m': 5,'f': 0,'p': -2,'s': -1,'t': -1,'w': -1,'y': -1,'v': 1,'b': -3,'z': -1,'x': -1},
        'f': {'a': -2,'r': -3,'n': -3,'d': -3,'c': -2,'q': -3,'e': -3,'g': -3,'h': -1,'i':  0,'l': 0,'k': -3,'m': 0,'f': 6,'p': -4,'s': -2,'t': -2,'w': 1,'y': 3,'v': -1,'b': -3,'z': -3,'x': -1},
        'p': {'a': -1,'r': -2,'n': -2,'d': -1,'c': -3,'q': -1,'e': -1,'g': -2,'h': -2,'i': -3,'l': -3,'k': -1,'m': -2,'f': -4,'p': 7,'s': -1,'t': -1,'w': -4,'y': -3,'v': -2,'b': -2,'z': -1,'x': -2},
        's': {'a':  1,'r': -1,'n':  1,'d':  0,'c': -1,'q':  0,'e':  0,'g':  0,'h': -1,'i': -2,'l': -2,'k': 0,'m': -1,'f': -2,'p': -1,'s': 4,'t': 1,'w': -3,'y': -2,'v': -2,'b': 0,'z': 0,'x': 0},
        't': {'a':  0,'r': -1,'n':  0,'d': -1,'c': -1,'q': -1,'e': -1,'g': -2,'h': -2,'i': -1,'l': -1,'k': -1,'m': -1,'f': -2,'p': -1,'s': 1,'t': 5,'w': -2,'y': -2,'v': 0,'b': -1,'z': -1,'x': 0},
        'w': {'a': -3,'r': -3,'n': -4,'d': -4,'c': -2,'q': -2,'e': -3,'g': -2,'h': -2,'i': -3,'l': -2,'k': -3,'m': -1,'f': 1,'p': -4,'s': -3,'t': -2,'w': 11,'y': 2,'v': -3,'b': -4,'z': -3,'x': -2},
        'y': {'a': -2,'r': -2,'n': -2,'d': -3,'c': -2,'q': -1,'e': -2,'g': -3,'h':  2,'i': -1,'l': -1,'k': -2,'m': -1,'f': 3,'p': -3,'s': -2,'t': -2,'w': 2,'y': 7,'v': -1,'b': -3,'z': -2,'x': -1},
        'v': {'a':  0,'r': -3,'n': -3,'d': -3,'c': -1,'q': -2,'e': -2,'g': -3,'h': -3,'i':  3,'l': 1,'k': -2,'m': 1,'f': -1,'p': -2,'s': -2,'t': 0,'w': -3,'y': -1,'v': 4,'b': -3,'z': -2,'x': -1},
        'b': {'a': -2,'r': -1,'n':  3,'d':  4,'c': -3,'q':  0,'e':  1,'g': -1,'h':  0,'i': -3,'l': -4,'k': 0,'m': -3,'f': -3,'p': -2,'s': 0,'t': -1,'w': -4,'y': -3,'v': -3,'b': 4,'z': 1,'x': -1},
        'z': {'a': -1,'r':  0,'n':  0,'d':  1,'c': -3,'q':  3,'e':  4,'g': -2,'h':  0,'i': -3,'l': -3,'k': 1,'m': -1,'f': -3,'p': -1,'s': 0,'t': -1,'w': -3,'y': -2,'v': -2,'b': 1,'z': 4,'x': -1},
        'x': {'a':  0,'r': -1,'n': -1,'d': -1,'c': -2,'q': -1,'e': -1,'g': -1,'h': -1,'i': -1,'l': -1,'k': -1,'m': -1,'f': -1,'p': -2,'s': 0,'t': 0,'w': -2,'y': -1,'v': -1,'b': -1,'z': -1,'x': -1},
}