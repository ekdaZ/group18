export default class Timer {
    constructor(root) {
        root.innerHTML = Timer.getHTML();

        this.el = {
            minutes: root.querySelector(".countdown--minutes"),
            seconds: root.querySelector(".countdown--seconds"),
            control: root.querySelector(".countdown__button--control"),
            reset: root.querySelector(".countdown__button--reset")
        };

        this.interval = null;
        this.remainingSeconds = 0;

        // This creates the functionality for the play and pause button when it is clicked on.
        this.el.control.addEventListener("click", () => {
            if (this.interval === null) {
                this.start();
            } else {
                this.stop();
            }
        });

        // This creates the prompt for the reset button when it is clicked on.
        this.el.reset.addEventListener("click", () => {
            const inputMinutes = prompt("Enter number of minutes: ");

            if (inputMinutes < 60) {
                this.stop();
                this.remainingSeconds = inputMinutes * 60;
                this.updateInterfaceTime();
            }
        });
    }

    // Updates the time on the clock.
    updateInterfaceTime() {
        const minutes = Math.floor(this.remainingSeconds / 60);
        const seconds = this.remainingSeconds % 60;

        this.el.minutes.textContent = minutes.toString().padStart(2, "0");
        this.el.seconds.textContent = seconds.toString().padStart(2, "0");
    }

    // Updates the icon on the start/stop button.
    updateInterfaceControls() {
        if (this.interval === null) {
            this.el.control.innerHTML = `<span class="material-icons">play_arrow</span>`;
            this.el.control.classList.add("countdown__button--start");
            this.el.control.classList.remove("countdown__button--stop");
        } else {
            this.el.control.innerHTML = `<span class="material-icons">pause</span>`;
            this.el.control.classList.add("countdown__button--stop");
            this.el.control.classList.remove("countdown__button--start");
        }
    }

    // Counts down until it hits zero.
    start() {
        if (this.remainingSeconds === 0) return;

        this.interval = setInterval(() => {
            this.remainingSeconds--;
            this.updateInterfaceTime();

            if (this.remainingSeconds === 0) {
                this.stop();
            }
        }, 1000);

        this.updateInterfaceControls();
    }

    // Stops counting down.
    stop() {
        clearInterval(this.interval);
        this.interval = null;
        this.updateInterfaceControls();
    }

    static getHTML() {
        return `
            <div class="inner__circle">
                <div>
                    <span class="countdown countdown--minutes">00</span>
                    <span class="countdown">:</span>
                    <span class="countdown countdown--seconds">00</span>
                </div>
                <div>
                    remaining...
                </div>
                <div>
                    <button type="button" class="countdown__button countdown__button--control countdown__button--start">
                        <span class="material-icons">play_arrow</span>
                    </button>
                    <button type="button" class="countdown__button countdown__button--control countdown__button--reset">
                        <span class="material-icons">timer</span>
                    </button>
                </div>
            </div>
        `;
    }
}

// Dom (2022) Codepen: Easy Countdown Timer with JavaScript [Source code].
// https://codepen.io/dcode-software/pen/XWgyOpg