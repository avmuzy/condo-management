function calc() {
  let apto201 = document.getElementById('201');
  let aptoNum201 = Number(apto201.value);
  let tx201 = document.getElementById('tx201');
  let txNum201 = Number(tx201.value);
  let total201 = aptoNum201 + txNum201;
  let res201 = document.getElementById('res201');
  res201.innerHTML = `${total201}`;

  let apto202 = document.getElementById('202');
  let aptoNum202 = Number(apto202.value);
  let tx202 = document.getElementById('tx202');
  let txNum202 = Number(tx202.value);
  let total202 = aptoNum202 + txNum202;
  let res202 = document.getElementById('res202');
  res202.innerHTML = `${total202}`;

  let apto301 = document.getElementById('301');
  let aptoNum301 = Number(apto301.value);
  let tx301 = document.getElementById('tx301');
  let txNum301 = Number(tx301.value);
  let total301 = aptoNum301 + txNum301;
  let res301 = document.getElementById('res301');
  res301.innerHTML = `${total301}`;

  let apto302 = document.getElementById('302');
  let aptoNum302 = Number(apto302.value);
  let tx302 = document.getElementById('tx302');
  let txNum302 = Number(tx302.value);
  let total302 = aptoNum302 + txNum302;
  let res302 = document.getElementById('res302');
  res302.innerHTML = `${total302}`;

  let apto401 = document.getElementById('401');
  let aptoNum401 = Number(apto401.value);
  let tx401 = document.getElementById('tx401');
  let txNum401 = Number(tx401.value);
  let total401 = aptoNum401 + txNum401;
  let res401 = document.getElementById('res401');
  res401.innerHTML = `${total401}`;

  let apto402 = document.getElementById('402');
  let aptoNum402 = Number(apto402.value);
  let tx402 = document.getElementById('tx402');
  let txNum402 = Number(tx402.value);
  let total402 = aptoNum402 + txNum402;
  let res402 = document.getElementById('res402');
  res402.innerHTML = `${total402}`;

  let apto501 = document.getElementById('501');
  let aptoNum501 = Number(apto501.value);
  let tx501 = document.getElementById('tx501');
  let txNum501 = Number(tx501.value);
  let total501 = aptoNum501 + txNum501;
  let res501 = document.getElementById('res501');
  res501.innerHTML = `${total501}`;

  let apto502 = document.getElementById('502');
  let aptoNum502 = Number(apto502.value);
  let tx502 = document.getElementById('tx502');
  let txNum502 = Number(tx502.value);
  let total502 = aptoNum502 + txNum502;
  let res502 = document.getElementById('res502');
  res502.innerHTML = `${total502}`;

  let totalapartamentos =
    total201 +
    total202 +
    total301 +
    total302 +
    total401 +
    total402 +
    total501 +
    total502;
  let totapto = document.querySelector('div#totapto');
  totapto.innerHTML = `Total apartamentos: ${totalapartamentos}`;
}
