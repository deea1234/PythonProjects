Python program that determines the image of a polygon in a plane through a reflection over a given line. 

Consider both cases: the line given by its general equation (input will be the coefficients of the equation), 
and the line given by a point and a direction vector. In the latter case, 
write the general equation first, starting from the point and direction vector.

The program should include the following steps:

1.Determine the intersection point of the line with one of the axes.
2.Determine the translation matrix that moves the line through the origin.
3.Determine the rotation matrix around the origin that aligns the line with one of the axes.
4.Determine the reflection matrix over the chosen coordinate axis.
5.Determine the rotation matrix around the origin that restores the line to its initial direction.
6.Determine the translation matrix that restores the line to its initial position.
7.Determine the composite transformation matrix by multiplying the five preceding matrices.
8.Read the vertices of the polygon.
9.Establish the homogeneous matrix of the transformed coordinates of the given polygon.

The program should include tests to determine if the line is parallel to one of the axes (in which case no rotation is needed), 
or passes through the origin (in which case no translation is needed). Similarly, if the line coincides with one of the axes, no rotation or translation is required.

Input data will be:

1.3 or 4 (indicating whether the line is given by its general equation or by a point and direction vector).
  If by general equation, expect three real numbers (coefficients a, b, c of the line equation ax + by + c = 0).
  If by point and direction vector, expect coordinates of the point and components of the direction vector.
2.Number of vertices of the polygon, an integer of at least 1.
3.Coordinates of the polygon vertices.

Output data will be:

1.The matrices of the five elementary transformations. Each matrix should be labeled accordingly. 
  If a transformation is not needed, indicate whether the line is vertical, horizontal, or passes through the origin.
2.The composite transformation matrix.
3.The homogeneous matrix of the transformed coordinates of the given polygon."
