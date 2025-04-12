package main

import (
    "net/http"

    "github.com/gin-gonic/gin"
)

func main() {
    r := gin.Default()

    // Define un endpoint GET
    r.GET("/ping", func(c *gin.Context) {
        c.JSON(http.StatusOK, gin.H{
            "message": "pong",
        })
    })

	// Define un endpoint GET para recibir una cadena
	r.GET("/saludo/:cadena", func(c *gin.Context) {
		cadena := c.Param("cadena")
		c.JSON(http.StatusOK, gin.H{
			"message": "Hola: " + cadena,
		})
	})

    // Define un endpoint POST
    r.POST("/data", func(c *gin.Context) {
        var jsonData map[string]interface{}
        if err := c.BindJSON(&jsonData); err != nil {
            c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
            return
        }
        c.JSON(http.StatusOK, gin.H{"received": jsonData})
    })

    // Inicia el servidor en el puerto 8080
    r.Run(":8080")
}