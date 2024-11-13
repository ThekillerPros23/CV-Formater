const FPDF = require('node-fpdf');

// Clase personalizada para agregar encabezado y pie de página
class PDF extends FPDF {
  // Encabezado
  Header() {
    // Establecer fuente
    this.SetFont('Arial', 'B', 12);
    // Título del encabezado
    this.Cell(0, 10, 'Este es el encabezado de la página', 0, 1, 'C');
    // Salto de línea
    this.Ln(10);
  }

  // Pie de página
  Footer() {
    // Posicionar a 1.5 cm del final
    this.SetY(-15);
    // Establecer fuente
    this.SetFont('Arial', 'I', 8);
    // Número de página
    this.Cell(0, 10, `Página ${this.PageNo()}`, 0, 0, 'C');
  }
}

// Crear un nuevo documento PDF
const pdf = new PDF();

// Agregar una página
pdf.AddPage();

// Establecer la fuente
pdf.SetFont('Arial', '', 16);

// Agregar texto
pdf.Cell(40, 10, '¡Hola, este es un PDF generado con node-fpdf!');

// Insertar una imagen (Asegúrate de tener la imagen en el directorio)
pdf.Image('Nature_107.jpg', 10, 50, 50, 50);

// Agregar más texto
pdf.Ln(100); // Salto de línea
pdf.Cell(40, 10, 'Este es otro texto debajo de la imagen.');

// Salvar el archivo PDF
pdf.Output('F', 'ejemplo.pdf');
