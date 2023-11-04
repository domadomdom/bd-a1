# Copy the output files to your local machine

docker cp d89e0495b936:/home/doc-bd-a1/res_dpre.csv ./service-result/
docker cp d89e0495b936:/home/doc-bd-a1/eda-in-1.txt ./service-result/
docker cp d89e0495b936:/home/doc-bd-a1/eda-in-2.txt ./service-result/
docker cp d89e0495b936:/home/doc-bd-a1/eda-in-3.txt ./service-result/
docker cp d89e0495b936:/home/doc-bd-a1/k.txt ./service-result/
docker cp d89e0495b936:/home/doc-bd-a1/vis.png ./service-result/

# Close the container
docker stop d89e0495b936
