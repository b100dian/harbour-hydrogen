#/bin/sh
git submodule update --init --recursive
cd hydrogen
yarn install
yarn build
cd ..
specify -Nns rpm/*yaml || exit 1
printf building...
rpmbuild -bb --build-in-place rpm/*.spec > build.log 2>&1
