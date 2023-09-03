let count = 0;

function cc(card) {
  // Only change code below this line
  switch (card) {
    case 2:
    case 3:
    case 4:
    case 5:
    case 6:
      count++;
      if (count == 5) {
        return "5 Bet";
      }
      break;

    case 7:
    case 8:
    case 9:
      count;
      if (count == 0) {
        return "0 Hold";
      }
      break;

    case 10:
    case 'J':
    case 'Q':
    case 'K':
    case 'A':
      count--;
      if (count == -5) {
        return "-5 Hold";
      }
      break;

    case 3:
    case  7:
    case 'Q':
    case  8:
    case 'A':
      count = -1;
      if (count == -1) {
        return "-1 Hold";
      }
      break;

    case 2:
    case 'J':
    case 9:
    case 2:
    case 7:
      count = 1;
      if (count == 1) {
        return "1 Bet";
      }
      break;


    case 2:
    case 2:
    case 10:
      count = 1;
      if (count == 1) {
        return "1 Bet";
      }
      break;



    case 3:
    case 2:
    case 'A':
    case 10:
    case 'K':
      count = -1;
      if (count == -1) {
        return "-1 Hold";
      }
      break;
  }

  // Only change code above this line
}

cc(2); cc(3); cc(7); cc('K'); cc('A');