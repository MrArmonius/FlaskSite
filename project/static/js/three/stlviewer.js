var camera, controls

function STLViewerEnable(classname) {
    var models = document.getElementsByClassName(classname);
    for (var i = 0; i < models.length; i++) {
        STLViewer(models[i], models[i].getAttribute("data-src"));
    }
}

function STLViewer(elem, model) {



    var renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    camera = new THREE.PerspectiveCamera(70, elem.clientWidth / elem.clientHeight, 1, 1000);
    camera.enableZoom;
    renderer.setSize(elem.clientWidth, elem.clientHeight);
    elem.appendChild(renderer.domElement);

    window.addEventListener('resize', function () {
        renderer.setSize(elem.clientWidth, elem.clientHeight);
        camera.aspect = elem.clientWidth / elem.clientHeight;
        camera.updateProjectionMatrix();
    }, false);

    controls = new THREE.OrbitControls(camera, renderer.domElement);
    controls.enableDamping = true;
    controls.rotateSpeed = 0.5;
    controls.dampingFactor = 0.1;
    controls.enableZoom = true;
    controls.enablePan = true;
    controls.autoRotate = true;
    controls.autoRotateSpeed = .75;

    var scene = new THREE.Scene();
    scene.background = new THREE.Color(0xf1f1f1);

    scene.add(new THREE.HemisphereLight(0xffffff, 0x080820, 1.25));

    const stlloader = new THREE.STLLoader();

    stlloader.load(model, function (geometry) {
        var material = new THREE.MeshPhongMaterial({ color: 0x248bfb, specular: 100, shininess: 100 });
        var mesh = new THREE.Mesh(geometry, material);
        scene.add(mesh);

        // Compute the middle
        var middle = new THREE.Vector3();
        var size = new THREE.Vector3();
        geometry.computeBoundingBox();
        geometry.boundingBox.getCenter(middle);
        geometry.boundingBox.getSize(size);

        // Center it
        mesh.position.x = (-1 * middle.x);
        mesh.position.y = (-1 * middle.y);
        mesh.position.z = (-1 * middle.z);

        // Pull the camera away as needed
        

        let bound_x = (geometry.boundingBox.max.x+Math.abs(geometry.boundingBox.min.x));
        let bound_y = (geometry.boundingBox.max.y+Math.abs(geometry.boundingBox.min.y));
        let bound_z = (geometry.boundingBox.max.z+Math.abs(geometry.boundingBox.min.z));

        var largestDimension = Math.max(bound_x,
            bound_y, bound_z);
        camera.position.z = largestDimension * 1;

        console.log("x: ", bound_x);
        console.log("y: ", bound_y);
        console.log("z: ", bound_z);
        console.log("LD: ", largestDimension);

        setDimension((Math.ceil((bound_x + Number.EPSILON) * 100) / 100), (Math.ceil((bound_y + Number.EPSILON) * 100) / 100),
            Math.ceil((bound_z + Number.EPSILON) * 100) / 100);

        controls.saveState();

        var animate = function () {
            requestAnimationFrame(animate);
            controls.update();
            renderer.render(scene, camera);
        }; animate();

    });

}

function setDimension(x_length, y_length, z_length) {
    var x_length_elements = document.getElementsByClassName("x_length");
    var y_length_elements = document.getElementsByClassName("y_length");
    var z_length_elements = document.getElementsByClassName("z_length");


    for (let element of x_length_elements) {
        
        element.textContent += x_length;
    }

    for (let element of y_length_elements) {
        element.textContent += y_length;
    }

    for (let element of z_length_elements) {
        element.textContent += z_length;
    }

}

function resetPositionCamera() {
    controls.reset();
}
