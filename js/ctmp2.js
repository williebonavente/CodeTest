// Function to add hours to a 24-hour time
function addHours(time, hours) {
    const [hoursStr, minutesStr] = time.split(':');
    let totalMinutes = parseInt(hoursStr) * 60 + parseInt(minutesStr);
    totalMinutes += hours * 60;
    totalMinutes = (totalMinutes + 1440) % 1440; // To handle 24-hour clock wrap-around
    const newHours = Math.floor(totalMinutes / 60);
    const newMinutes = totalMinutes % 60;
    return `${String(newHours).padStart(2, '0')}:${String(newMinutes).padStart(2, '0')}`;
  }
  
  // Function to subtract hours from a 24-hour time
  function subtractHours(time, hours) {
    return addHours(time, -hours);
  }
  
  // a) 100 hours after it reads 2:00?
  const timeA = '2:00';
  const timeAAfter100Hours = addHours(timeA, 100);
  console.log(`a) 100 hours after ${timeA} is ${timeAAfter100Hours}`);
  
  // b) 45 hours before it reads 12:00?
  const timeB = '12:00';
  const timeBBefore45Hours = subtractHours(timeB, 45);
  console.log(`b) 45 hours before ${timeB} is ${timeBBefore45Hours}`);
  
  // c) 168 hours after it reads 19:00?
  const timeC = '19:00';
  const timeCAfter168Hours = addHours(timeC, 168);
  console.log(`c) 168 hours after ${timeC} is ${timeCAfter168Hours}`);
  