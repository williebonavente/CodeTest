// Testing

let x = 0;


function cc(card)
{
    switch (card) {
        case 2:
        case 3:
        case 4:
            x = 5; 
            if (x ==5) {
                return "5 Hold";
            }
            break;
        case 3:
        case 4:
        case 5:
            x = -5; 
            if (x == -5) {
                return "-5 Bet";
            }
    
        default:
            break;
    }
}

console.log(cc(5));
