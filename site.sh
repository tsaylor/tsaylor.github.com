#!/bin/sh
# https://www.grymoire.com/Unix/Sh.html
case $1 in
    build | b )
        docker run --rm --volume="$PWD:/srv/jekyll" -it jekyll/jekyll:latest jekyll build
        ;;
    serve | server | s )
        docker run --rm --volume="$PWD:/srv/jekyll" --publish 4000:4000 jekyll/jekyll jekyll serve
        ;;
    shell | sh )
        docker run --rm -it --volume="$PWD:/srv/jekyll" --publish 4000:4000 jekyll/jekyll /bin/bash
        ;;
    * )
        echo "unrecognized command"
        ;;
esac

