const fs = require('fs');

// Read the contest of a file
const filePath =  "C:/Users/USER/OneDrive/Desktop/Temp/Random_Programming/trash_codes-1/texts/text1.txt"
fs.readFile(filePath,'utf8',(err, data) => {
    if(err) throw err;
    console.log(data);
});