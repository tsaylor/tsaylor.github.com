#!/bin/sh
# https://www.grymoire.com/Unix/Sh.html
case $1 in
    build | b )
        python md_to_html.py
        ;;
    serve | server | s )
        python -m http.server --directory=build
        ;;
    clean | c )
        rm -rf build
        ;;
    * )
        echo "unrecognized command"
        ;;
esac

