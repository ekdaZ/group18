class Timer {

    constructor(time) {
        this.interval = null;
        this.remainingSeconds = time;
    }

    // Updates the time on the clock.
    updateInterfaceTime() {
        const hours = Math.floor(this.remainingSeconds/3600)
        const minutes = Math.floor(this.remainingSeconds / 60);
        const seconds = this.remainingSeconds % 60;
        console.log(hours + "h "
                    + minutes + "m " + seconds + "s ")
    }

    // Counts down until it hits zero.
    start() {
        this.interval = setInterval(() => {
            this.remainingSeconds--;
            this.updateInterfaceTime();

            if (this.remainingSeconds === 0) {
                this.stop();
            }
        }, 1000);
    }

    // Stops counting down.
    stop() {
        clearInterval(this.interval);
        this.interval = null;
        // this.updateInterfaceControls();
    }
}


function timer(){
    const timer = new Timer(65);
    timer.start();
    console.log('kjnhhb v');
}

