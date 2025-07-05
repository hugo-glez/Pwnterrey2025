echo "---------------------------------"
echo " Extraer informaci'on de URSA VBS"
echo "---------------------------------"
echo " PARAM1 : nombre del archivo vbs"
echo " PARAM2 : nombre de la funcion de decodificacion"
echo "---------------------------------"
echo "---------------------------------"

FVBS="$1"
Ffunc="$2"

cp $FVBS file.vbs
grep $2 file.vbs | grep '=' | grep '"' > data.txt
python3 ../de.py > replaces.bash
bash replaces.bash
grep 'http' file.vbs
