a=readcvs('IceCreamData.csv')
scatter(a(:,1),a(:,2),'filled')
m=mean(a);
std_feature=std(a);
## import the satistics module 
norm_pdf_x=normpdf(a(:,1),mean_feature(:,1),std_feature )
norm_pdf_y=normpdf(a(:,2), mean_feature(:,2),std_feature)
overall=norm_pdf_x.*norm_pdf_y;
figure;
scatter(a(:,1),a(:,2), 70,overall, 'filled')
threshold_value=0.01;
colorbar;
outlier_set=overall<threshold_value;
hold on;

detected=a(outlier_set,:);
scatter(detected(:,1),detected (:,2), 70, "red", "filled")