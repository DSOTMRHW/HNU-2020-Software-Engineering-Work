namespace WinFormsApp1
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        Point oriPoint;
        private void button1_MouseDown(object sender, MouseEventArgs e)

        {

            oriPoint = e.Location;

        }
        private void button1_MouseMove(object sender, MouseEventArgs e)

        {

            if (e.Button == MouseButtons.Left)//如果按下了鼠标左键

            {

                Button b = sender as Button;

                //当前位置等于鼠标移动前的位置加上和起始位置的差距

                b.Location = new Point(b.Location.X + (e.X - oriPoint.X), b.Location.Y + (e.Y - oriPoint.Y));

            }

        }
    }
}