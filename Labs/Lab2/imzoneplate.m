function I = imzoneplate(N)

%   Descri??o
%
%   I = imzoneplate gera uma imagem de teste "zone-plate" de dimens?es 501-by-501.
%   I = imzoneplate(N) gera uma imagem de teste "zone-plate" com dimens?oes N-by-N.
%
%   A imagem gerada consiste num padr?o radialmente sim?trico com baixas frequ?ncias 
%   no centro as quais v?o aumentando em direc??o aos bordos da imagem, exibindo as 
%   mais altas frequ?ncias nos cantos da imagem.
%
%   Exemplos
%
%   Criar e mostrar uma  imagem de teste com as dimens~?es por omiss?o (501-by-501).
%
%       I = imzoneplate;
%       imshow(I)
%
%   Criar uma imagem mais pequena e apresentar metade da imagem no ?cran.
%
%       I = imzoneplate(151);
%       plot(I(76,:))
%
%   REFER?NCIAS
%
%   Bernd Jhne, "Practical Handbook on Image Processing for Scientific Applications".
%   CRC Press, 1997. Equa??o 10.63:
%
%   g({\bf x}) = g_0 \sin\left(\frac{k_m|{\bf x}|^2}{2r_m}\right) 
%   \left[\frac{1}{2} \tanh\left(\frac{r_m-|{\bf x}|}{w}\right) + 
%   \frac{1}{2}\right]
%
%   Nesta equa??o, g assume valores dentro do intervalo [-1,1]. A fun??o imzoneplate
%   retorna I = (g+1)/2, o qual assume valores no intervalo [0,1].
%
%   Ver tamb?m  http://blogs.mathworks.com/steve/2011/07/19/jahne-test-pattern-take-3/

%   Copyright 2012 The MathWorks, Inc.
%   Steven L. Eddins

if nargin < 1
    N = 501;
end

if rem(N,2) == 1
    x2 = (N-1)/2;
    x1 = -x2;
else
    x2 = N/2;
    x1 = -x2 + 1;
end

[x,y] = meshgrid(x1:x2);
r = hypot(x,y);
km = 0.7*pi;
rm = x2;
w = rm/10;
term1 = sin( (km * r.^2) / (2 * rm) );
term2 = 0.5*tanh((rm - r)/w) + 0.5;
g = term1 .* term2;

I = (g + 1)/2;