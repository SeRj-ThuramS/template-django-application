import sys
import os

import app

if __name__ == "__main__":
    app.env.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    app.Init(sys.argv[1:])
