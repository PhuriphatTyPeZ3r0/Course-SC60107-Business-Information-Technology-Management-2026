import os

test_html = """<!DOCTYPE html>
<html>
<head>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/controls/OrbitControls.js"></script>
<script src="https://cdn.jsdelivr.net/npm/three@0.128.0/examples/js/loaders/GLTFLoader.js"></script>
<style>
body { margin: 0; background: #0c162e; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; color: white; font-family: sans-serif; }
#canvasBox { width: 500px; height: 500px; position: relative; }
canvas { width: 100%; height: 100%; display: block; }
.controls { margin-top: 10px; display: flex; gap: 8px; }
button { padding: 6px 14px; border-radius: 6px; border: 1px solid #38bdf8; background: #1e293b; color: white; cursor: pointer; }
button:hover { background: #2563eb; }
</style>
</head>
<body>
<div id="canvasBox"><canvas id="c"></canvas></div>
<div class="controls">
  <button onclick="renderModel('ชีสเค้ก')">ชีสเค้ก (Cheesecake)</button>
  <button onclick="renderModel('ลาเต้')">ลาเต้ (Latte Cup)</button>
  <button onclick="renderModel('ครัวซองต์')">ครัวซองต์ (Croissant)</button>
  <button onclick="renderModel('ชาไทย')">ชาไทยเย็น (Iced Drink)</button>
  <button onclick="renderModel('บราวนี')">บราวนี (Brownie)</button>
</div>

<script>
let scene, camera, renderer, controls, group;

function init() {
  const box = document.getElementById('canvasBox');
  scene = new THREE.Scene();
  scene.background = new THREE.Color(0x0c162e);

  camera = new THREE.PerspectiveCamera(40, 1, 0.1, 100);
  camera.position.set(0, 3.5, 5.5);

  renderer = new THREE.WebGLRenderer({ canvas: document.getElementById('c'), antialias: true });
  renderer.setSize(500, 500);
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  renderer.shadowMap.enabled = true;
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1.2;

  controls = new THREE.OrbitControls(camera, renderer.domElement);
  controls.enableDamping = true;

  // Studio Lights
  const ambient = new THREE.AmbientLight(0xffffff, 0.7);
  scene.add(ambient);

  const keyLight = new THREE.DirectionalLight(0xffffff, 1.4);
  keyLight.position.set(5, 8, 5);
  scene.add(keyLight);

  const fillLight = new THREE.PointLight(0x38bdf8, 2, 10);
  fillLight.position.set(-4, 3, 3);
  scene.add(fillLight);

  const rimLight = new THREE.PointLight(0xf97316, 2, 10);
  rimLight.position.set(4, 2, -3);
  scene.add(rimLight);

  group = new THREE.Group();
  scene.add(group);

  // Pedestal
  const baseGeo = new THREE.CylinderGeometry(2.2, 2.3, 0.15, 48);
  const baseMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.3, metalness: 0.8 });
  const base = new THREE.Mesh(baseGeo, baseMat);
  base.position.y = -0.075;
  group.add(base);

  const ringGeo = new THREE.TorusGeometry(2.25, 0.03, 16, 48);
  const ringMat = new THREE.MeshBasicMaterial({ color: 0x38bdf8 });
  const ring = new THREE.Mesh(ringGeo, ringMat);
  ring.rotation.x = Math.PI / 2;
  ring.position.y = 0.02;
  group.add(ring);

  renderModel('ชีสเค้ก');
  animate();
}

function clearCurrentModel() {
  while (group.children.length > 2) {
    group.remove(group.children[2]);
  }
}

function renderModel(type) {
  clearCurrentModel();
  const m = new THREE.Group();

  if (type === 'ชีสเค้ก') {
    // 1. Ceramic Dessert Plate
    const plateGeo = new THREE.CylinderGeometry(1.8, 1.5, 0.08, 48);
    const plateMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.15, metalness: 0.1 });
    const plate = new THREE.Mesh(plateGeo, plateMat);
    plate.position.y = 0.04;
    m.add(plate);

    // 2. Triangular Wedge Cake Slice
    const shape = new THREE.Shape();
    shape.moveTo(0, 0);
    shape.lineTo(1.6, -0.65);
    shape.quadraticCurveTo(1.75, 0, 1.6, 0.65);
    shape.lineTo(0, 0);

    const extrudeSettings = { depth: 0.8, bevelEnabled: true, bevelSegments: 3, steps: 1, bevelSize: 0.04, bevelThickness: 0.04 };
    const sliceGeo = new THREE.ExtrudeGeometry(shape, extrudeSettings);
    sliceGeo.center();

    // Graham Cracker Crust (Bottom)
    const crustMat = new THREE.MeshStandardMaterial({ color: 0x9a5a2a, roughness: 0.8 });
    const crust = new THREE.Mesh(sliceGeo, crustMat);
    crust.scale.set(1.02, 1.02, 0.25);
    crust.rotation.x = Math.PI / 2;
    crust.position.set(0, 0.16, 0);
    m.add(crust);

    // Cream Cheese Body (Middle)
    const cheeseMat = new THREE.MeshStandardMaterial({ color: 0xfffae8, roughness: 0.3 });
    const cheese = new THREE.Mesh(sliceGeo, cheeseMat);
    cheese.scale.set(1, 1, 0.7);
    cheese.rotation.x = Math.PI / 2;
    cheese.position.set(0, 0.52, 0);
    m.add(cheese);

    // Strawberry Glaze (Top)
    const glazeMat = new THREE.MeshStandardMaterial({ color: 0xd91e36, roughness: 0.1, metalness: 0.2 });
    const glaze = new THREE.Mesh(sliceGeo, glazeMat);
    glaze.scale.set(1.01, 1.01, 0.1);
    glaze.rotation.x = Math.PI / 2;
    glaze.position.set(0, 0.85, 0);
    m.add(glaze);

    // Berry on Top
    const berryGeo = new THREE.DodecahedronGeometry(0.18, 1);
    const berryMat = new THREE.MeshStandardMaterial({ color: 0x990000, roughness: 0.2 });
    const berry = new THREE.Mesh(berryGeo, berryMat);
    berry.position.set(0.2, 0.98, 0);
    m.add(berry);

  } else if (type === 'ลาเต้' || type === 'คาปูชิโน' || type === 'อเมริกาโน') {
    // 1. Ceramic Saucer
    const saucerGeo = new THREE.CylinderGeometry(1.6, 1.3, 0.08, 48);
    const saucerMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.15, metalness: 0.1 });
    const saucer = new THREE.Mesh(saucerGeo, saucerMat);
    saucer.position.y = 0.04;
    m.add(saucer);

    // Saucer Lip
    const lipGeo = new THREE.TorusGeometry(1.5, 0.04, 16, 48);
    const lip = new THREE.Mesh(lipGeo, saucerMat);
    lip.rotation.x = Math.PI / 2;
    lip.position.y = 0.08;
    m.add(lip);

    // 2. Ceramic Coffee Cup Body
    const cupGeo = new THREE.CylinderGeometry(1.05, 0.75, 1.15, 48);
    const cupMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.15, metalness: 0.1 });
    const cup = new THREE.Mesh(cupGeo, cupMat);
    cup.position.y = 0.65;
    m.add(cup);

    // Cup Rim
    const rimGeo = new THREE.TorusGeometry(1.05, 0.05, 16, 48);
    const rim = new THREE.Mesh(rimGeo, cupMat);
    rim.rotation.x = Math.PI / 2;
    rim.position.y = 1.22;
    m.add(rim);

    // 3. Ergonomic Handle
    const handleGeo = new THREE.TorusGeometry(0.38, 0.08, 16, 32, Math.PI * 1.3);
    const handle = new THREE.Mesh(handleGeo, cupMat);
    handle.rotation.z = -Math.PI / 6;
    handle.position.set(1.15, 0.65, 0);
    m.add(handle);

    // 4. Coffee Liquid
    const isAmericano = (type === 'อเมริกาโน');
    const coffeeColor = isAmericano ? 0x2b1704 : 0x784a27;
    const coffeeGeo = new THREE.CylinderGeometry(0.98, 0.98, 0.05, 36);
    const coffeeMat = new THREE.MeshStandardMaterial({ color: coffeeColor, roughness: 0.15 });
    const coffee = new THREE.Mesh(coffeeGeo, coffeeMat);
    coffee.position.y = 1.15;
    m.add(coffee);

    // 5. Latte Art Foam
    if (!isAmericano) {
      const foamGeo = new THREE.RingGeometry(0.1, 0.6, 32);
      const foamMat = new THREE.MeshStandardMaterial({ color: 0xfffae8, roughness: 0.4, side: THREE.DoubleSide });
      const foam = new THREE.Mesh(foamGeo, foamMat);
      foam.rotation.x = -Math.PI / 2;
      foam.position.y = 1.18;
      m.add(foam);

      const heartGeo = new THREE.CircleGeometry(0.25, 32);
      const heart = new THREE.Mesh(heartGeo, foamMat);
      heart.rotation.x = -Math.PI / 2;
      heart.position.y = 1.181;
      m.add(heart);
    }

  } else if (type === 'ครัวซองต์') {
    // 1. Ceramic Serving Plate
    const plateGeo = new THREE.CylinderGeometry(1.7, 1.4, 0.08, 48);
    const plateMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.15, metalness: 0.1 });
    const plate = new THREE.Mesh(plateGeo, plateMat);
    plate.position.y = 0.04;
    m.add(plate);

    // 2. Crescent Croissant Curved Body
    const croissantGroup = new THREE.Group();
    const segmentCount = 9;
    for (let i = 0; i < segmentCount; i++) {
      const t = (i / (segmentCount - 1)) - 0.5; // -0.5 to 0.5
      const angle = t * Math.PI * 0.9;
      const radius = 1.0;
      const x = Math.sin(angle) * radius;
      const z = (Math.cos(angle) * radius * 0.65) - 0.5;
      
      const thickness = Math.cos(t * Math.PI) * 0.42 + 0.1;
      const segGeo = new THREE.SphereGeometry(thickness, 18, 18);
      segGeo.scale(1, 1.1, 1.35);

      const crustColor = (i % 2 === 0) ? 0xcc7722 : 0xd9822b;
      const segMat = new THREE.MeshStandardMaterial({ color: crustColor, roughness: 0.6 });
      const seg = new THREE.Mesh(segGeo, segMat);
      seg.position.set(x, 0.38 + thickness * 0.2, z);
      seg.rotation.y = -angle;
      croissantGroup.add(seg);
    }
    m.add(croissantGroup);

  } else if (type === 'บราวนี') {
    // 1. Plate
    const plateGeo = new THREE.CylinderGeometry(1.6, 1.4, 0.08, 48);
    const plateMat = new THREE.MeshStandardMaterial({ color: 0xf8fafc, roughness: 0.15 });
    const plate = new THREE.Mesh(plateGeo, plateMat);
    plate.position.y = 0.04;
    m.add(plate);

    // 2. Fudge Brownie Cube
    const brownieGeo = new THREE.BoxGeometry(1.3, 0.65, 1.3);
    const brownieMat = new THREE.MeshStandardMaterial({ color: 0x3d1c06, roughness: 0.75 });
    const brownie = new THREE.Mesh(brownieGeo, brownieMat);
    brownie.position.y = 0.4;
    m.add(brownie);

    // Chocolate Glaze Top
    const glazeGeo = new THREE.BoxGeometry(1.32, 0.08, 1.32);
    const glazeMat = new THREE.MeshStandardMaterial({ color: 0x241103, roughness: 0.2, metalness: 0.3 });
    const glaze = new THREE.Mesh(glazeGeo, glazeMat);
    glaze.position.y = 0.75;
    m.add(glaze);

    // Walnut / Nut chips on top
    for (let i = 0; i < 4; i++) {
      const nutGeo = new THREE.DodecahedronGeometry(0.09);
      const nutMat = new THREE.MeshStandardMaterial({ color: 0xc19a6b, roughness: 0.6 });
      const nut = new THREE.Mesh(nutGeo, nutMat);
      nut.position.set((Math.random() - 0.5) * 0.7, 0.82, (Math.random() - 0.5) * 0.7);
      m.add(nut);
    }

  } else {
    // Cold Drink: ชาไทย / โกโก้
    const isThaiTea = (type === 'ชาไทย');
    const liquidColor = isThaiTea ? 0xe65100 : 0x4a2c1d;

    // 1. Coaster Base
    const coasterGeo = new THREE.CylinderGeometry(1.2, 1.2, 0.06, 36);
    const coasterMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 0.4 });
    const coaster = new THREE.Mesh(coasterGeo, coasterMat);
    coaster.position.y = 0.03;
    m.add(coaster);

    // 2. Glass Body
    const glassGeo = new THREE.CylinderGeometry(0.85, 0.68, 1.85, 32);
    const glassMat = new THREE.MeshPhysicalMaterial({
      color: 0xffffff,
      transparent: true,
      opacity: 0.35,
      roughness: 0.05,
      metalness: 0.1,
      transmission: 0.85,
      ior: 1.5
    });
    const glass = new THREE.Mesh(glassGeo, glassMat);
    glass.position.y = 0.98;
    m.add(glass);

    // 3. Liquid inside
    const liqGeo = new THREE.CylinderGeometry(0.8, 0.64, 1.6, 32);
    const liqMat = new THREE.MeshStandardMaterial({ color: liquidColor, roughness: 0.2 });
    const liquid = new THREE.Mesh(liqGeo, liqMat);
    liquid.position.y = 0.88;
    m.add(liquid);

    // Milk froth on top
    const frothGeo = new THREE.CylinderGeometry(0.81, 0.81, 0.15, 32);
    const frothMat = new THREE.MeshStandardMaterial({ color: 0xfffbeb, roughness: 0.3 });
    const froth = new THREE.Mesh(frothGeo, frothMat);
    froth.position.y = 1.68;
    m.add(froth);

    // 4. Ice Cubes floating
    const iceGeo = new THREE.BoxGeometry(0.35, 0.35, 0.35);
    const iceMat = new THREE.MeshPhysicalMaterial({ color: 0xffffff, transparent: true, opacity: 0.7, roughness: 0.1, transmission: 0.9 });
    
    const ice1 = new THREE.Mesh(iceGeo, iceMat);
    ice1.position.set(0.15, 1.72, 0.1);
    ice1.rotation.set(0.3, 0.4, 0.2);
    m.add(ice1);

    const ice2 = new THREE.Mesh(iceGeo, iceMat);
    ice2.position.set(-0.2, 1.7, -0.15);
    ice2.rotation.set(0.1, 0.8, 0.3);
    m.add(ice2);

    // 5. Drinking Straw
    const strawGeo = new THREE.CylinderGeometry(0.04, 0.04, 2.3, 16);
    const strawMat = new THREE.MeshStandardMaterial({ color: 0x38bdf8, roughness: 0.3 });
    const straw = new THREE.Mesh(strawGeo, strawMat);
    straw.position.set(0.2, 1.4, 0);
    straw.rotation.z = -0.22;
    straw.rotation.x = 0.15;
    m.add(straw);
  }

  group.add(m);
}

function animate() {
  requestAnimationFrame(animate);
  if (controls) controls.update();
  if (group) group.rotation.y += 0.006;
  if (renderer && scene && camera) renderer.render(scene, camera);
}

init();
</script>
</body>
</html>"""

with open('02_Labs_Assignments/auction-quad-dashboard/test_models.html', 'w', encoding='utf-8') as f:
    f.write(test_html)

print("Saved test_models.html!")
