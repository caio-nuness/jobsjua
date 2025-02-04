# jobsjua

## 1 Fix
- Quando o usuario está deslogando... não está deslogando de fato
- so está movendo para a tela de login da pra visualizar pq não muda 
- o botão de login e logout 

## 2 Fix
- desenvolver as rotas internas liberadas apenas para as empresas
- para VER uma unica vaga e para CRIAR uma nova vaga e DELETAR 

## 3 Fix
- Tanto no secret quanto no padão, resolver a questão do ID davaga que 
- ta sendo passado como parametro todas estão ficando com o mesmo id

buscar ID com  
   empresa = request.user

   vagas = Vacancie.objects.all()
   vagas.id
   print()

