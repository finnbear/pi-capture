cd /home/pi/git/pi-capture
timeout 1434m python main.py
cd gallery
cd  "$(\ls -1dt ./*/ | head -n 1)"
cd  "$(\ls -1dt ./*/ | head -n 1)"
cd  "$(\ls -1dt ./*/ | head -n 1)"
ffmpeg -framerate 30 -f image2 -s 480x480 -pattern_type glob -i '*.jpg' -pix_fmt yuv420p -crf 1 -vb 10M day.avi -y
if [ $? -eq 0 ]; then
    find "$PWD" -type f -name "day.avi" -exec bash -c ' DIR=$( dirname "{}"  ); mv "{}" "$DIR"/"../${DIR##*/}".avi ' \;
    rm -rf *.jpg
    cd ..
    find . -type d -empty -delete
fi
