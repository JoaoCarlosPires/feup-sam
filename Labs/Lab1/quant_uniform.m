% Este programa faz a quantiza??o de um sinal audio n?o comprimido.
% Recebe como parametros os nomes dos ficheiros de entrada e saida e o numerado e niveis de quantizacao
% Programa adaptado da fun??o ?quant_uniform.m de Yao Wang, Polytechnic University, 2/11/2004

function []=quant_uniform(ficheiroEntrada,ficheiroSaida, N) 

if nargin < 3
disp('Utilizacao: quant_uniform(nome_ficheiro_entrada, nome_ficheiro_saida, numero de nivei');
disp('ficheiroEntrada: nome de um ficheiro wave');
disp('ficheiroSaida: nome de um ficheiro wave para escreve o som resultante'); 
disp('N: inteiro com numero de knives de quantizacao');
end;

%importar para x um ficheiro de som (representado com 16 bits e fs)
[x,fs]=audioread(ficheiroEntrada);

%verificar numero de canais (estereo ou mono). Se estereo, usar apenas um
%canal (adicionado em Fev 2022)
info=audioinfo(ficheiroEntrada);
if info.NumChannels>1
    x=x(:,1);
end

% calcular passo de quantizacao para o número N de níveis indicado
magmax=max(abs(x)); 
xmin=-magmax; xmax=magmax;
Q=(xmax-xmin)/N; 
disp('xmin,xmax,N,Q'); 
disp([xmin,xmax,N,Q]);

%aplicar quantizacao uniforme a cada amostra do sinal de entrada e gravar
xq=floor((x-xmin)/Q)*Q+Q/2+xmin;
audiowrite(ficheiroSaida,int16(xq),fs); 

%comparar qualidade do som original  quantizado
sound(x,fs);
fprintf('\n Prima uma tecla para continuar');
pause;
sound(xq,fs);

% plot sobreposto das formas de onda ao um intervalo reduzido
% correspondente a 1/500 das amostras
% original a vermelho com : e quantizado a azul com _
t=1:length(x)/512;
figure, axis tight, plot(t,x(1:length(t)),'r*'); %title('original');
hold on; 
plot(t,xq(1:length(t)),'b-'), title('1/500 do numero total das amostras dos sinais original e quantizado');
legend('original a vermelho','quantizado a azul');

%plot da forma de onda no intervalo correspondente às amostras t=2000:2200;
t=2000:2200;
fprintf('\n\nLet now look at the signal in the interval [%g  - %g]sec\n\n',2000/fs,2200/fs);
fprintf('\n Prima uma tecla para continuar');
pause;

figure; plot(t,x(2000:2200),'r*'); hold on; plot(t,xq(2000:2200),'b-'); axis tight; grid on;
legend('original a vermelho','quantizado a azul'), 
title('intervalo correspondente a 200 amostras dos sinais original e quantizado');

% calcular o MSE e PSNR
D=x-xq;
MSE=mean(D.^2);
MSE2 = sum(sum((x - xq).^2))/N;
MAXx=max(x);
PSNR = 10*log10((double(MAXx^2))/MSE2);
fprintf('\nErro entre o sinal original e o interpolado = %g\n\n',MSE);
fprintf('\nPSNR do sinal interpolado = %g\n\n',PSNR);