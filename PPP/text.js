var retezec = "";
var slovo = "";
var pozice = 0;
var pravda_lez = "";

function najdi_slovo() {
    retezec = document.getElementById('tpole_retezec').value;
    slovo = document.getElementById('tpole_slovo').value;
    pozice = retezec.search(slovo) + 1;
    console.log(pozice);
    if (pozice > 0) {
        pravda_lez = "JE";
    }
    else {
        pravda_lez = "NENÍ";
    }
    console.log(pravda_lez);
    document.getElementById('odpoved').textContent = pravda_lez;
}