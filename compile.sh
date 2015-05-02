FREELANCER_DIR=./startbootstrap-freelancer
cp -R $FREELANCER_DIR/css ./production/
cp -R $FREELANCER_DIR/fonts ./production/
cp -R $FREELANCER_DIR/font-awesome ./production/
cp -R $FREELANCER_DIR/js ./production/

mkdir -p ./production/css
lessc ./source/less/freelancer.less > ./production/css/freelancer.css
cp ./source/js/* ./production/js/
cp -R ./source/img ./production/
cd ./production
python -m SimpleHTTPServer