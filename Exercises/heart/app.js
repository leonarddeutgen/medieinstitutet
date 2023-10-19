const countdown = () => {
    const countDate = new Date('October 19, 2023 00:00:00').getTime();
    const now = new Date().getTime();
    const gap = countDate - now;

    // how the fuck does time work?
    const second = 1000;
    const minutes = second * 60
    const hours = minutes * 60
    const day = hours * 24

    // Calculate it
    const textDay = Math.floor(gap /day);
    const textHour = Math.floor((gap % day) / hours);
    const textMinute = Math.floor((gap % hours) / minutes);
    const textSecond = Math.floor((gap % minutes) / second);

    document.querySelector('.day').innerText = textDay;
    document.querySelector('.hour').innerText = textHour;
    document.querySelector('.minute').innerText = textMinute;
    document.querySelector('.second').innerText = textSecond;
};


setInterval(countdown,1000)
