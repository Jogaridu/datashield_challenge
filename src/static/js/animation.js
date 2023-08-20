let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');

var colorStatus = localStorage.getItem('dtsldColorStatus') ?? "D11400";

checkbox.addEventListener("change", () => {

    colorStatus = checkbox.checked ? "0B7314" : "D11400";
    localStorage.setItem('dtsldColorStatus', colorStatus);

    color.addColorStop(0.1, `#${colorStatus}46`);
    color.addColorStop(0.049, `#${colorStatus}0D`);
    resizeCanvas();

});

let vertices = 90;
let amplitude = 30;
let color = ctx.createLinearGradient(0, 0, canvas.width, canvas.height);
color.addColorStop(0.1, `#${colorStatus}46`);
color.addColorStop(0.049, `#${colorStatus}0D`);
let time = 0;

function createSphere(radius, xCenter, yCenter) {
    let points = [];
    for (let i = 0; i <= vertices; i++) {
        let angle1 = i / vertices * Math.PI * 2;
        let x1 = Math.cos(angle1) * radius + xCenter;
        let y1 = Math.sin(angle1) * radius + yCenter;
        points.push({ x: x1, y: y1 });
    }
    return points;
}

let spheres = [];

function update() {
    time += 0.03;
}

function render() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = color;
    ctx.lineWidth = 1;
    ctx.lineCap = 'round';

    for (let i = 0; i < spheres.length; i++) {
        let sphere = spheres[i];
        for (let j = 0; j < sphere.length; j++) {
            let point = sphere[j];
            let waveRadius;
            if (i < 30) {
                waveRadius = (i + 1) / 60 * amplitude * Math.cos(j / vertices * Math.PI * 700 + time);
            } else {
                waveRadius = (i + 1) / 1000 * amplitude * Math.cos(j / vertices * Math.PI * 700 + time);
            }
            let x = point.x + Math.cos(j / vertices * Math.PI * 8 + time) * waveRadius;
            let y = point.y + Math.sin(j / vertices * Math.PI * 8 + time) * waveRadius;
            if (j === 0) {
                ctx.beginPath();
                ctx.moveTo(x, y);
            } else {
                ctx.lineTo(x, y);
            }
        }
        ctx.stroke();
    }

}

function resizeCanvas() {
    canvas.width = 550;
    canvas.height = 550;
    spheres = [];


    for (let i = 0; i < 30; i++) {
        let radius = 10 + 5 * i;
        let xCenter = canvas.width / 2 + Math.sin(i / 60 * Math.PI * 2)
        let yCenter = canvas.height / 2 + Math.cos(i / 80 * Math.PI * 2);
        spheres.push(createSphere(radius, xCenter, yCenter));
    }
    for (let i = 0; i < 40; i++) {
        let radius = 130 + 0.5 * i;
        let xCenter = canvas.width / 2 + 30 * Math.cos(i / 60 * Math.PI * 2);
        let yCenter = canvas.height / 2 - 27 * Math.sin(i / 80 * Math.PI * 2);
        spheres.push(createSphere(radius, xCenter, yCenter));
    }
    for (let i = 0; i < 50; i++) {
        let radius = 140 + 0.8 * i;
        let xCenter = canvas.width / 2 + 39 * Math.cos(i / 70 * Math.PI * 2);
        let yCenter = canvas.height / 2 - 90 * Math.sin(i / 800 * Math.PI * 2);
        spheres.push(createSphere(radius, xCenter, yCenter));
    }
    for (let i = 0; i < 80; i++) {
        let radius = 150 + 0.8 * i;
        let xCenter = canvas.width / 2 + 45 * Math.cos(i / 70 * Math.PI * 2);
        let yCenter = canvas.height / 2 - 40 * Math.sin(i / 800 * Math.PI * 2);
        spheres.push(createSphere(radius, xCenter, yCenter));
    }
    for (let i = 0; i < 100; i++) {
        let radius = 180 + 0.7 * i;
        let xCenter = canvas.width / 2 - 35 * Math.cos(i / 80 * Math.PI * 2);
        let yCenter = canvas.height / 2 + 30 * Math.sin(i / 150 * Math.PI * 2);
        spheres.push(createSphere(radius, xCenter, yCenter));
    }
}

resizeCanvas();
// window.addEventListener('resize', resizeCanvas);

function animate() {
    update();
    render();
    requestAnimationFrame(animate);
}

animate();