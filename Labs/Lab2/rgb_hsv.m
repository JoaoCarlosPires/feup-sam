function rgb_hsv(originalPicture);

O=imread(originalPicture);
if contains(originalPicture,"elephant.bmp",'IgnoreCase',true) 
    O = cat(3, O, O, O);
end
I=im2double(O);

R=I(:,:,1);
G=I(:,:,2);
B=I(:,:,3);

figure(1); 
subplot(2,3,2),imshow(I); title('original picture');
subplot(2,3,4),imshow(R); title('R component');
subplot(2,3,5),imshow(G); title('G component');
subplot(2,3,6),imshow(B); title('B component');

% conversion to HSV

HSV = rgb2hsv(O);
[h,s,v] = imsplit(HSV);

figure(2); 
subplot(2,3,2),imshow(HSV); title('HSV picture');
subplot(2,3,4),imshow(h); title('H component');
subplot(2,3,5),imshow(s); title('S component');
subplot(2,3,6),imshow(v); title('V component');

