function calc() {
  let apto = document.getElementById('condapto');
  let aptoNum = Number(apto.value);
  let txextra = document.getElementById('txextra');
  let txNum = Number(txextra.value);
  let total = aptoNum + txNum;
  let res = document.getElementById('res');
  res.innerHTML = `${total}`;
}
