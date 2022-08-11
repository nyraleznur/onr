let x=1;

while(x<=3){
  usu=prompt("digite su usuario")
  con=prompt("digite su contraseña")
  if(usu=="pepe"&& con=="123"){
    alert("ok bienvenido")
    x=4;
  }
  else{
    alert("te quedan "+(x-1)+"intentos")
  }

}

if(x==3){
  alert("bloqueado")
}

