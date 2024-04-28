// constructor function

function HouseKeeper (years,nameofman,duty);
    this.years =years;
    this.nameofman = nameofman;
    this.duty = duty;
    this.play = function() {
        //code
    }
}

var housekeeper1 = new HouseKeeper (1,2,bala); // ini ngebuat data salah satu HK

housekeeper1.play(); // play adalah salah satu data yang terkanduung, dan dieksekusi oleh HK1

