#version 120

uniform mat4 projection;
uniform mat4 view;
uniform mat4 model;

attribute vec3 position;
attribute vec3 normal;  // Add the normal attribute

varying vec3 fragNormal;  // Pass the transformed normal to the fragment shader

void main() {
    gl_Position = projection * view * model * vec4(position, 1.0);
    fragNormal = (transpose(inverse(mat3(model))) * normal).xyz;  // Transform the normal
}
