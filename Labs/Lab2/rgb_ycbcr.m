function rgb_ycbcr(originalPicture);

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

% conversion to YCBCR

YCBCR = rgb2ycbcr(O);
[y,cb,cr] = imsplit(YCBCR);

figure(2); 
subplot(2,3,2),imshow(YCBCR); title('YCBCR picture');
subplot(2,3,4),imshow(y); title('Y component');
subplot(2,3,5),imshow(cb); title('CB component');
subplot(2,3,6),imshow(cr); title('CR component');

